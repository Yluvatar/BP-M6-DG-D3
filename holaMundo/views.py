from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(
        """
        <h1>HOME DE LA PÁGINA</h1>

        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi ipsum corrupti enim eaque blanditiis placeat repudiandae deleniti suscipit aspernatur tenetur vel necessitatibus, tempore quia cupiditate reprehenderit dignissimos magni fugiat asperiores?</p>

        """
    )


def about(request):
    return HttpResponse(
        """

        <h1>About US</h1>

        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas earum, facilis perspiciatis veritatis fuga nostrum. Aliquid, quos quae. Ea odit magni atque earum exercitationem consectetur voluptates odio voluptatum tempore quisquam?</p>

        """
    )


def contact(request):
    return HttpResponse(
        """
        <h2>Formulario de Contacto</h2>
        <form action="/submit_formulario" method="post">
            <label for="nombre">Nombre:</label><br>
            <input type="text" id="nombre" name="nombre" required><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br>
            <label for="mensaje">Mensaje:</label><br>
            <textarea id="mensaje" name="mensaje" rows="4" required></textarea><br>
            <input type="submit" value="Enviar">
        </form>

        """
    )