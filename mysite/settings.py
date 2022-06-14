from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))
# DEBUG = False

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',           # django-bootstrap4
    'django_summernote',
    'import_export',
    'django.forms',
    
    'accounts.apps.AccountsConfig',
    'myinfo',
    'django_cleanup',
    'imagekit',
    # 'bootstrap_toolkit',
    'mysched',
    'sample',
    'myreport',
    # 'bootstrap_datepicker_plus',
    # 'grappelli',
    # 'filebrowser',
    'tinymce',
    'dbbackup',  # django-dbbackup 追加
    # 'ajax_datatable',
    'myprofit',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mysite.middleware.login_required.LoginRequiredMiddleware' # ←これを追加
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myinfo.context_processors.my_context_processor', # 追加
                'myreport.context_processors.my_context_processor', # 追加
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django',
#         'USER': 'django',
#         'PASSWORD': 'django',
#         'HOST': 'db',
#         'PORT': 3306,
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("SQL_DATABASE"), 
        'USER': os.environ.get("SQL_USER"),
        'PASSWORD' : os.environ.get("SQL_PASSWORD"),
        'HOST' : os.environ.get("SQL_HOST"),
        'PORT' : os.environ.get("SQL_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True
# DATE_FORMAT = 'Y-m-d'
# USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# #bs4sampleで追加
# STATICFILES_DIRS =(
#     os.path.join(BASE_DIR,'static'),
# )

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

SUMMERNOTE_THEME = 'bs4'
X_FRAME_OPTOPNS = 'SAMEORIGIN'


# """ summernote画像や動画を保存するディレクトリ """
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# """ サマーノートの設定 """
SUMMERNOTE_THEME = 'bs4'
SUMMERNOTE_CONFIG = {
    'summernote': {
        'width': '100%',
        'height': '480',
        'lang': "ja-JP",

        'toolbar': [
            ['do', ['undo', 'redo']],
            ['style', ['style']],
            ['color', ['color']],
            ['font', ['bold', 'underline', 'strikethrough', 'clear']],
            ['fontname', ['fontname', 'fontsize']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video', 'hr']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],

    },
}


#とりあえずログ出力設定　https://is.gd/8GCTgJ　エラーなので一旦中止
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'dark',
    messages.ERROR: 'danger',
}

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

AUTH_USER_MODEL = 'accounts.User'


#↓は管理サイトのTimyMCE。アプリの設定はuploader.js内に記述
# TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    "height": "400px",
    "menubar": "edit format insert view table help",
    "plugins": "visualblocks template searchreplace hr code autosave advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste code help wordcount emoticons image",
    "toolbar": "undo redo | bold underline forecolor backcolor emoticons removeformat | fontsizeselect formatselect | outdent indent | alignleft aligncenter alignright | numlist bullist | image media insertfile hr link | preview fullscreen code visualblocks searchreplace",
    "file_picker_types": "image media",
    "image_class_list": [
        {"title": 'Responsive', "value": 'img-fluid'}
    ],
    "forced_root_block": '',

}
# TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")
# FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
DATA_UPLOAD_MAX_MEMORY_SIZE = 800000
ATTACHMENT_MAX_IMAGE_UPLOAD_SIZE = 800000
ATTACHMENT_MAX_FILE_UPLOAD_SIZE = 800000

# 追加
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# BASE_DIR/backups/にバックアップファイルを保存する設定
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, 'backups')}
# 最新の3つのファイルを保存(それより古いものは順番に破棄)する設定
DBBACKUP_CLEANUP_KEEP = 6
# メディアのバックアップファイルも同様の設定
DBBACKUP_CLEANUP_KEEP_MEDIA = 6