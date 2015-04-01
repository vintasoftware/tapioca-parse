# coding: utf-8

RESOURCE_MAPPING = {
    'class': {
        'resource': 'classes/{name}/{id}',
        'methods': ['GET', 'PUT', 'DELETE'],
        'docs': 'https://www.parse.com/docs/rest#objects-creating'
    },
    'classes': {
        'resource': 'classes/{name}',
        'methods': ['GET', 'POST'],
        'docs': 'https://www.parse.com/docs/rest#objects-creating'
    },
    'login': {
        'resource': 'login',
        'methods': ['GET'],
        'docs': 'https://www.parse.com/docs/rest#users-login'
    },
    'logout': {
        'resource': 'logout',
        'methods': ['POST'],
        'docs': 'https://www.parse.com/docs/rest#sessions-deleting'
    },
    'user': {
        'resource': 'users/{id}',
        'methods': ['GET', 'PUT', 'DELETE'],
        'docs': 'https://www.parse.com/docs/rest#users-retrieving',
        'extra_docs': ['https://www.parse.com/docs/rest#users-validating'],
    },
    'users': {
        'resource': 'users',
        'methods': ['GET', 'POST'],
        'docs': 'https://www.parse.com/docs/rest#users-signup',
        'extra_docs': ['https://www.parse.com/docs/rest#users-querying'],
    },
    'password_reset': {
        'resource': 'requestPasswordReset',
        'methods': ['POST'],
        'docs': 'https://www.parse.com/docs/rest#users-passwordreset'
    },
    'session': {
        'resource': 'sessions/{id}',
        'methods': ['GET', 'PUT', 'DELETE'],
        'docs': 'https://www.parse.com/docs/rest#sessions-retrieving'
    },
    'sessions': {
        'resource': 'sessions',
        'methods': ['GET', 'POST'],
        'docs': 'https://www.parse.com/docs/rest#sessions-creating',
        'extra_docs': ['https://www.parse.com/docs/rest#sessions-querying'],
    },
    'role': {
        'resource': 'roles/{id}',
        'methods': ['GET', 'PUT', 'DELETE'],
        'docs': 'https://www.parse.com/docs/rest#roles-retrieving'
    },
    'roles': {
        'resource': 'roles',
        'methods': ['GET', 'POST'],
        'docs': 'https://www.parse.com/docs/rest#roles-creating'
    },
    'file_upload': {
        'resource': 'files/{name}',
        'methods': ['POST'],
        'docs': 'https://www.parse.com/docs/rest#files-uploading'
    },
    'events': {
        'resource': 'events/{name}',
        'methods': ['POST'],
        'docs': 'https://www.parse.com/docs/rest#analytics-custom'
    },
    'event_app_opened': {
        'resource': 'events/AppOpened',
        'methods': ['POST'],
        'docs': 'https://www.parse.com/docs/rest#analytics'
    },
    'push_notifications': {
        'resource': 'push',
        'methods': ['POST'],
        'docs': 'https://www.parse.com/docs/push_guide#top/REST'
    },
    'installation': {
        'resource': 'installations/{id}',
        'methods': ['GET', 'PUT', 'DELETE'],
        'docs': 'https://www.parse.com/docs/rest#installations-retrieving'
    },
    'installations': {
        'resource': 'installations',
        'methods': ['GET', 'POST'],
        'docs': 'https://www.parse.com/docs/rest#installations-uploading',
        'extra_docs': ['https://www.parse.com/docs/rest#installations-querying'],
    },
    'function': {
        'resource': 'functions/{name}',
        'methods': ['POST'],
        'docs': 'https://www.parse.com/docs/rest#cloudfunctions'
    },
    'job': {
        'resource': 'jobs/{name}',
        'methods': ['POST'],
        'docs': 'https://www.parse.com/docs/rest#backgroundjobs'
    },
}
