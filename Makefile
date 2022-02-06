run-staging-env:
	heroku config:set DJANGO_SETTINGS_MODULE=core.settings.heroku \
	&& heroku config:set SECRET_KEY="django-insecure-d=dx&eu7ey(ophx@_p-15damar_tc@^v-8uo&devaj9qhh%*k(" \
	&& heroku config:set DISABLE_COLLECTSTATIC=1 \
	&& heroku run python manage.py makemigrations  \
	&& heroku run python manage.py migrate

run-dev:
	python manage.py runserver

create-superuser:
	heroku run python manage.py createsuperuser