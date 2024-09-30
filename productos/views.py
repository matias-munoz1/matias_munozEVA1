from django.shortcuts import render

def usuario(request):
    return render(request, 'productos/usuario.html')

def identificacion_usuario(request):
    return render(request, 'productos/usuario.html')

def productos(request):
    return render(request, 'productos/productos.html')


def electronica(request):
    return render(request, 'productos/electronica.html')

def ropa(request):
    return render(request, 'productos/ropa.html')

def detalle_telefono(request):
    return render(request, 'productos/detalle_telefono.html')

def detalle_portatil(request):
    return render(request, 'productos/detalle_portatil.html')

def detalle_tablet(request):
    return render(request, 'productos/detalle_tablet.html')

def juguetes(request):
    return render(request, 'productos/juguetes.html')

def detalle_juguete(request):
    return render(request, 'productos/detalle_jugete.html')

def ropa(request):
    return render(request, 'productos/ropa.html')

def detalle_ropa(request):
    return render(request, 'productos/detalle_ropa.html')

def detalle_auto(request):
    return render(request, 'productos/detalle_auto.html')

def detalle_muneca(request):
    return render(request, 'productos/detalle_muneca.html')

def detalle_bloques(request):
    return render(request, 'productos/detalle_bloques.html')

def detalle_chaqueta(request):
    return render(request, 'productos/detalle_chaqueta.html')

def detalle_camiseta(request):
    return render(request, 'productos/detalle_camiseta.html')

def detalle_jeans(request):
    return render(request, 'productos/detalle_jeans.html')

from django.http import HttpResponse

def index(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MatiSHOP - Inicio</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
            }
            .category-card {
                background-color: #e9ecef;
                border: none;
                padding: 20px;
                transition: background-color 0.3s ease-in-out;
                text-align: center;
            }
            .category-card:hover {
                background-color: #007bff;
                color: #fff;
            }
            .category-card a {
                color: inherit;
                text-decoration: none;
            }
            .carousel-inner img {
                height: 500px;
                object-fit: cover;
            }
        </style>
    </head>
    <body>


        <!-- Navegación -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="/">MatiSHOP</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/">Inicio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/usuario/">Identificación de Usuario</a>
                    </li>
                </ul>
            </div>
        </nav>

        <!-- Categorías de Productos -->
        <div class="container mt-5">
            <h2 class="text-center mb-4">Categorías Disponibles</h2>
            <div class="row">
                <div class="col-md-4">
                    <div class="category-card">
                        <a href="/productos/electronica/">
                            <div>
                                <h5>Electrónica</h5>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="category-card">
                        <a href="/productos/juguetes/">
                            <div>
                                <h5>Juguetes</h5>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="category-card">
                        <a href="/productos/ropa/">
                            <div>
                                <h5>Ropa</h5>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Carrusel de Imágenes -->
        <div id="carouselExampleIndicators" class="carousel slide mt-5" data-ride="carousel">
            <ol class="carousel-indicators">
                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="d-block w-100" alt="Ofertas">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Las Mejores Ofertas</h5>
                        <p>Encuentra descuentos en productos de todas las categorías.</p>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="https://images.unsplash.com/photo-1592475609592-5185f62cfb34?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="d-block w-100" alt="Nuevos Productos">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Nuevos Productos</h5>
                        <p>Lo último en tecnología y moda.</p>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="https://images.unsplash.com/photo-1441984904996-e0b6ba687e04?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="d-block w-100" alt="Calidad Garantizada">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Calidad Garantizada</h5>
                        <p>Productos seleccionados para ofrecer la mejor calidad.</p>
                    </div>
                </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Anterior</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Siguiente</span>
            </a>
        </div>

        <!-- Footer -->
        <footer class="bg-light mt-5 py-4 text-center">
            <div class="container">
                <p class="mb-0">© 2024 MatiSHOP. Todos los derechos reservados.</p>
            </div>
        </footer>

        

        <!-- Scripts -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)
