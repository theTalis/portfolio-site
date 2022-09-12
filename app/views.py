from django.shortcuts import render

def home(request):
    data = {
        "projects": [
            {
                "image": "/static/img/aplicativo.png",
                "description": "Crediario digital",
                "link": "https://crediario.digital",
                "text": "projecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdprojecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdprojecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdpaokwd pawokdpaowkdapowkdp aokwd paokwd paokwd poawk"
            },
            {
                "image": "/static/img/banking.png",
                "description": "T2 Banking",
                "link": "https://app.t2bank.com.br",
                "text": "projecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdprojecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdprojecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdpaokwd pawokdpaowkdapowkdp aokwd paokwd paokwd poawk"
            },
            {
                "image": "/static/img/emprestimo.png",
                "description": "Credito com vc",
                "link": "https://credito.com.vc",
                "text": "projecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdprojecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdprojecto coisado bastante trabalho coisa e tal e vai e tome e adwojdpoajwdoajwdoijawdojawd apowkdpaokwd pawokdpaowkdapowkdp aokwd paokwd paokwd poawk"
            }
        ]
    }
    return render(request, 'home.html', data)