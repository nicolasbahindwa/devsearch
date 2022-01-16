from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, EmptyPage
from .models import Project, Tag
from django.db.models import Q
from django.contrib import messages
from .forms import ProjectForm, ReviewForm
from utils.search import searchProjects
from utils.paginator import paginateProjects



projectList = [
        {
            'id': '1',
            'title': 'website design',
            'description': "ecommerce website full equiped"
        },
        {
            'id': '1',
            'title': 'website design',
            'description': "ecommerce website full equiped"
        },
        {
            'id': '1',
            'title': 'website design',
            'description': "ecommerce website full equiped"
        }
    ]
# Create your views here.


def projects(request):
    # return HttpResponse('Here are our projects')
    # msg = "hello welcome to the project"
    # number = 22
    # context = {'msg': msg, 'number': number, 'projects': projectList}
    # search_query = ''
    # if request.GET.get('search_query'):
    #     search_query = request.GET.get('search_query')

    # tags = Tag.objects.filter(name__icontains=search_query)
    # # projects = Project.objects.all()
    # projects = Project.objects.distinct().filter(
    #     Q(title__icontains=search_query) |
    #     Q(description__icontains=search_query) |
    #     Q(owner__name__icontains=search_query) |
    #     Q(tags__in=tags)
    # )
    projects, search_query = searchProjects(request)
    # pagination
    # end bug fix for pagination
    custom_range, projects = paginateProjects(request, projects, 3)

    context = {'projects': projects,
               'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


# prassing variable to a function
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        # update project count
        projectObj.getVoteCount
        messages.success(request, 'Thanks for your review')
        return redirect('project', pk=projectObj.id)
    context = {'projectObj': projectObj, 'form': form}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        # bug fix
        newtags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')
        print(request, 'Error')
        messages.error(request, "Error")
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    # project = Project.objects.get(id=pk)
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # bug fix
        newtags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {'form': form, 'project': project}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    # project = Project.objects.get(id=pk)
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)



 