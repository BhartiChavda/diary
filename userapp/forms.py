from django import forms
from .models import User, Note, Category, Contact

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-5 rounded-2xl input-premium font-bold',
        'placeholder': '••••••••'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-5 rounded-2xl input-premium font-bold',
        'placeholder': '••••••••'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'profile_pic', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'Specialist ID'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'name@network.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': '+91 00000 00000',
                'maxlength': '15'
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium file:bg-white file:text-black file:border-0 file:px-6 file:py-2 file:rounded-xl file:mr-6 file:font-black file:uppercase file:text-[10px] file:tracking-widest hover:file:bg-gray-200 cursor-pointer',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold',
                'placeholder': '••••••••'
            }),
            'confirm_password': forms.PasswordInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold',
                'placeholder': '••••••••'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove spaces, dashes, parentheses
            clean_number = ''.join(c for c in phone if c.isdigit())
            # If it starts with a country code (like 91), check if the rest is 10 digits
            if len(clean_number) < 10:
                raise forms.ValidationError("Mobile number must be at least 10 digits.")
            # Standardizing to the last 10 digits for the core number
            if len(clean_number) > 10 and not phone.startswith('+'):
                 # If no + prefix but more than 10 digits, assume it includes country code
                 pass 
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'file', 'content', 'category', 'reminder_date', 'is_archived', 'is_shared']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'Document Title'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold uppercase tracking-widest text-xs',
            }),
            'file': forms.FileInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium file:bg-white file:text-black file:border-0 file:px-6 file:py-2 file:rounded-xl file:mr-6 file:font-black file:uppercase file:text-[10px] file:tracking-widest hover:file:bg-gray-200 cursor-pointer',
            }),
            'reminder_date': forms.DateTimeInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'type': 'datetime-local'
            }),
            'is_archived': forms.CheckboxInput(attrs={'class': 'w-6 h-6 rounded-lg text-indigo-600 focus:ring-indigo-500 border-slate-200'}),
            'is_shared': forms.CheckboxInput(attrs={'class': 'w-6 h-6 rounded-lg text-indigo-600 focus:ring-indigo-500 border-slate-200'}),
        }

class NoteWriteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'reminder_date', 'is_archived', 'is_shared']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'Note Topic'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-medium leading-relaxed',
                'placeholder': 'Write your thoughts here...',
                'rows': 8
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold uppercase tracking-widest text-xs',
            }),
            'reminder_date': forms.DateTimeInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'type': 'datetime-local'
            }),
            'is_archived': forms.CheckboxInput(attrs={'class': 'w-6 h-6 rounded-lg text-indigo-600 focus:ring-indigo-500 border-slate-200'}),
            'is_shared': forms.CheckboxInput(attrs={'class': 'w-6 h-6 rounded-lg text-indigo-600 focus:ring-indigo-500 border-slate-200'}),
        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'profile_pic']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': '+91 00000 00000',
                'maxlength': '15'
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium file:bg-white file:text-black file:border-0 file:px-6 file:py-2 file:rounded-xl file:mr-6 file:font-black file:uppercase file:text-[10px] file:tracking-widest hover:file:bg-gray-200 cursor-pointer',
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            clean_number = ''.join(c for c in phone if c.isdigit())
            if len(clean_number) < 10:
                raise forms.ValidationError("Mobile number must be at least 10 digits.")
        return phone

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'profile_image', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'Your Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-bold tracking-wide',
                'placeholder': '+91 00000 00000',
                'maxlength': '15'
            }),
            'profile_image': forms.FileInput(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium file:bg-white file:text-black file:border-0 file:px-6 file:py-2 file:rounded-xl file:mr-6 file:font-black file:uppercase file:text-[10px] file:tracking-widest hover:file:bg-gray-200 cursor-pointer',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full p-5 rounded-2xl input-premium font-medium leading-relaxed',
                'placeholder': 'Tell us something...',
                'rows': 4
            }),
        }
