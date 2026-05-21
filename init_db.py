import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BatchPro.settings')
django.setup()

from userapp.models import User, Category

def init_db():
    # Create superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123', is_verified=True)
        print("Superuser 'admin' created (password: admin123)")

    # Create default categories
    categories = ['Education', 'Business', 'Personal', 'Technology', 'Science']
    for cat_name in categories:
        Category.objects.get_or_create(name=cat_name)
    print("Default categories created.")

if __name__ == '__main__':
    init_db()
