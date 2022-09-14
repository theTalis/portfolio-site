from django.shortcuts import render

def home(request):
    data = {
        "projects": [
            {
                "image": "/static/img/aplicativo.png",
                "title": "Crediário digital",
                "link": "https://crediario.digital/store",
                "color": "#33E0A1",
                "description": "Crediário Digital is a native mobile application developed with a focus on the retail customer of physical stores in order to enable the customer to make payments remotely in the best Buy now pay later style"
            },
            {
                "image": "/static/img/banking.png",
                "title": "T2 Banking",
                "link": "https://app.t2bank.com.br",
                "color": "#000000",
                "description": "T2Banking is a platform for processing payments made through pix and boleto, with statement and transfer control"
            },
            {
                "image": "/static/img/emprestimo.png",
                "title": "Credito com vc",
                "link": "https://credito.com.vc",
                "color": "#F8E14C",
                "description": "Credito.com.vc is a platform from which retail customers can purchase personal loans directly in the store"
            }
        ]
    }
    return render(request, 'home.html', data)

def send_email(request):
    """Envia email """
    return render(request, 'home.html')