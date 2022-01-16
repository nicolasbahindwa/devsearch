==== QUERIES ===================

(env) PS F:\Python_Programming\2022 python and Django\devproject\devsearch> python manage.py shell
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from projects.models import Project
>>> projects = Project.objects.all()
>>> print(projects)
<QuerySet [<Project: ecommerce webiste2022-01-09 05:37:45.288280+00:00>, <Project: Block chain for financial farms2022-01-09 06:18:41.375334+00:00>, <Project: Websocket for chat apps2022-01-09 06:19:43.660793+00:00>]>
>>>
>>> projectobj = Project.objects.get(title="Block chain for financial farms")
>>>
>>> print(projectobj)
Block chain for financial farms2022-01-09 06:18:41.375334+00:00
>>>
>>> print(projectobj.create_at)
2022-01-09 06:18:41.375334+00:00
>>>
>>> projects = Project.objects.filter(title__startswith="Bl")
>>>
>>> print(projects)
<QuerySet [<Project: Block chain for financial farms2022-01-09 06:18:41.375334+00:00>]>
>>>
>>> projects = Project.objects.filter(vote_ratio__gte=50)
>>> print(projects)
<QuerySet []>

>>> projects = Project.objects.filter(vote_ratio__gt=50)
>>> print(projects)
<QuerySet []>
>>> projects = Project.objects.filter(vote_ratio__lt=50)
>>> print(projects)
<QuerySet [<Project: ecommerce webiste2022-01-09 05:37:45.288280+00:00>, <Project: Block chain for financial farms2022-01-09 06:18:41.375334+00:00>, <Project: Websocket for chat apps2022-01-09 06:19:43.660793+00:00>]>
>>> projects = Project.objects.filter(vote_ratio__lte=50)
>>> print(projects)
<QuerySet [<Project: ecommerce webiste2022-01-09 05:37:45.288280+00:00>, <Project: Block chain for financial farms2022-01-09 06:18:41.375334+00:00>, <Project: Websocket for chat apps2022-01-09 06:19:43.660793+00:00>]>
>>>

>>> project = Project.objects.get(title="Websocket for chat apps")
>>>
>>> print(project)
Websocket for chat apps2022-01-09 06:19:43.660793+00:00
>>>
>>> print(project.review_set.all())
<QuerySet [<Review: up>]>
>>>
>>>
>>>
>>> print(project.tags.all())
<QuerySet [<Tag: JavaScript>, <Tag: Flask>]>
>>>