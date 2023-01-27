from django.shortcuts import render
import random

from password_generator_web.web.forms import UniquePassForm, EncryptionPass


class PassUniqueGenerator:
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOL = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def __init__(self, letters: int, symbols: int, numbers: int):
        self.letters = letters
        self.symbols = symbols
        self.numbers = numbers
        self.password_list = []

    def choice(self):
        for char in range(1, self.letters + 1):
            self.password_list.append(random.choice(self.LETTERS))
        for char in range(1, self.symbols + 1):
            self.password_list.append(random.choice(self.SYMBOL))
        for char in range(1, self.numbers + 1):
            self.password_list.append(random.choice(self.NUMBERS))

    def generated_pass(self):
        random.shuffle(self.password_list)
        password_for_print = ""
        for char in self.password_list:
            password_for_print += char
        return password_for_print


def encrypting(text, shift):
    plain_text = ""
    for ch in text:
        plain_text += chr(ord(ch) + shift)

    return plain_text


# Create your views here.
def index_page(request):
    return render(request, 'index_page.html')


def generate_unique_pass(request):
    if request.method == 'GET':
        form = UniquePassForm()
    else:
        form = UniquePassForm(request.POST)

        if form.is_valid():
            nr_letters = form.cleaned_data['number_of_letters']
            nr_numbers = form.cleaned_data['number_of_numbers']
            nr_symbols = form.cleaned_data['number_of_symbols']

            password = PassUniqueGenerator(nr_letters, nr_symbols, nr_numbers)
            password.choice()

            password_for_print = password.generated_pass()
            context = {'password': password_for_print}

            return render(request, 'success_generated_password.html', context)
    context = {
        'form': form,

    }
    return render(request, 'generate_password.html', context)


def encrypt_password(request):
    if request.method == 'GET':
        form = EncryptionPass()
    else:
        form = EncryptionPass(request.POST)

        if form.is_valid():
            user_password = form.cleaned_data['your_password']
            key_to_encrypt = form.cleaned_data['encrypter_key']

            password = encrypting(user_password, key_to_encrypt)
            context = {'password': password}

            return render(request, 'success_encrypted_password.html', context)
    context = {
        'form': form,

    }
    return render(request, 'encrypt_password.html', context)
