from django.core.context_processors import csrf

from django.shortcuts import render_to_response, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from wsgiref.util import FileWrapper

from fileServer.models import Document
from fileServer.forms import DocumentForm

import os.path

# Displays the login page
def loginView(request):
    c = {}
    c.update(csrf(request))

    return render_to_response('login.html', c)

# Authenticates a logging in user
def authLogin(request):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/login/')

# Logs out current user
def authLogout(request):
    logout(request)
    return redirect('/')

# Creates a new user
def createUser(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()

    return user

# Checks whether or not an existing user has the provided user name
def doesUserExist(username):
    user_count = User.objects.filter(username=username).count()

    if user_count == 0:
        return False

    return True

# Signs up a new user if needed and passes to authLogin
def authSignup(request):
    post = request.POST

    if not doesUserExist(post['email']):
        user = createUser(username=post['email'], email=post['email'], password=post['password'])

    return authLogin(request)

@login_required(login_url='/login/')
def managerView(request):
    # Handle file upload
    if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)

		if form.is_valid():
			newdoc = Document(docfile=form.cleaned_data['docfile'])
			newdoc.username = request.user.username
			newdoc.save()

		# Redirect to the document list after POST
		return HttpResponseRedirect(reverse('fileServer.views.managerView'))
    else:
        form = DocumentForm()

        # Load documents for the list page
        documents = [document for document in Document.objects.all() if request.user.username in document.docfile.name]

        # Render list page with the documents and the form
        return render_to_response(
            'fileManager.html',
            {'documents': documents, 'form': form},
            context_instance=RequestContext(request)
        )

@login_required(login_url='/login/')
def downloadFile(request):
	fileName = request.GET.get('f', 'nope')
	filePath = 'media/' + fileName
	print file(filePath)

	if os.path.isfile(filePath):
		wrapper = FileWrapper(file(filePath))
		response = HttpResponse(wrapper, content_type='text/plain')
		response['Content-Length'] = os.path.getsize(filePath)
		return response
	else:
		return redirect('/')
