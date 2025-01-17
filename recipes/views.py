# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'recipes/Home.html')


# Define recipes
RECIPES = [
    {"ingredients": ["pollo", "pasta", "tomate"], "recipe": "Pollo a la bolognesa con pasta.", "link": "https://example.com/pollo-bolognesa"},
    {"ingredients": ["arroz", "pollo", "brócoli"], "recipe": "Arroz con pollo y brócoli.", "link": "https://example.com/arroz-pollo-brocoli"},
    {"ingredients": ["zanahoria", "cebolla", "papa"], "recipe": "Ensalada de zanahoria, cebolla y papa.", "link": "https://example.com/ensalada-zanahoria-cebolla-papa"},
    {"ingredients": ["atún", "maíz", "lechuga"], "recipe": "Ensalada de atún con maíz y lechuga.", "link": "https://example.com/ensalada-atun-maiz-lechuga"},
    {"ingredients": ["queso", "tomate", "albahaca"], "recipe": "Pizza de queso con tomate y albahaca.", "link": "https://example.com/pizza-queso-tomate-albahaca"},
    {"ingredients": ["huevo", "espinacas", "queso"], "recipe": "Omelette de espinacas y queso.", "link": "https://example.com/omelette-espinacas-queso"},
    {"ingredients": ["salmón", "limón", "perejil"], "recipe": "Salmón al horno con limón y perejil.", "link": "https://example.com/salmon-horno-limon-perejil"},
    {"ingredients": ["frijoles", "tomate", "cebolla"], "recipe": "Frijoles refritos con tomate y cebolla.", "link": "https://example.com/frijoles-tomate-cebolla"},
    {"ingredients": ["pechuga de pollo", "limón", "ajo"], "recipe": "Pechuga de pollo al limón con ajo.", "link": "https://example.com/pechuga-pollo-limon-ajo"},
    {"ingredients": ["calabacín", "tomate", "queso"], "recipe": "Calabacín al horno con tomate y queso.", "link": "https://example.com/calabacin-horno-tomate-queso"},
    {"ingredients": ["garbanzos", "pepino", "pimiento"], "recipe": "Ensalada de garbanzos con pepino y pimiento.", "link": "https://example.com/ensalada-garbanzos-pepino-pimiento"},
    {"ingredients": ["camarones", "ajo", "limón"], "recipe": "Camarones al ajillo con limón.", "link": "https://example.com/camarones-ajillo-limon"},
    {"ingredients": ["papa", "cebolla", "aceite de oliva"], "recipe": "Papas al horno con cebolla y aceite de oliva.", "link": "https://example.com/papas-horno-cebolla-aceite-oliva"},
    {"ingredients": ["palta", "tomate", "cilantro"], "recipe": "Guacamole con tomate y cilantro.", "link": "https://example.com/guacamole-tomate-cilantro"},
    {"ingredients": ["espaguetis", "salsa de carne", "queso"], "recipe": "Espaguetis con salsa de carne y queso.", "link": "https://example.com/espaguetis-salsa-carne-queso"},
    {"ingredients": ["brócoli", "zanahoria", "soja"], "recipe": "Salteado de brócoli, zanahoria y soja.", "link": "https://example.com/salteado-brocoli-zanahoria-soja"},
    {"ingredients": ["huevo", "pimiento", "cebolla"], "recipe": "Huevos revueltos con pimientos y cebolla.", "link": "https://example.com/huevos-revueltos-pimientos-cebolla"},
    {"ingredients": ["pollo", "lima", "jengibre"], "recipe": "Pollo a la parrilla con lima y jengibre.", "link": "https://example.com/pollo-parrilla-lima-jengibre"},
    {"ingredients": ["calabaza", "mantequilla", "canela"], "recipe": "Puré de calabaza con mantequilla y canela.", "link": "https://example.com/pure-calabaza-mantequilla-canela"},
    {"ingredients": ["champiñones", "ajo", "mantequilla"], "recipe": "Champiñones salteados con ajo y mantequilla.", "link": "https://example.com/champinones-salteados-ajo-mantequilla"},
    {"ingredients": ["manzana", "canela", "azúcar"], "recipe": "Compota de manzana con canela.", "link": "https://example.com/compota-manzana-canela"},
    {"ingredients": ["arroz", "leche", "vainilla"], "recipe": "Arroz con leche y vainilla.", "link": "https://example.com/arroz-con-leche-vainilla"},
    {"ingredients": ["pollo", "miel", "mostaza"], "recipe": "Pollo al horno con miel y mostaza.", "link": "https://example.com/pollo-horno-miel-mostaza"},
    {"ingredients": ["zanahoria", "jengibre", "naranja"], "recipe": "Sopa de zanahoria con jengibre y naranja.", "link": "https://example.com/sopa-zanahoria-jengibre-naranja"},
    {"ingredients": ["lentejas", "tomate", "pimiento"], "recipe": "Guiso de lentejas con tomate y pimiento.", "link": "https://example.com/guiso-lentejas-tomate-pimiento"},
    {"ingredients": ["batata", "miel", "canela"], "recipe": "Batatas al horno con miel y canela.", "link": "https://example.com/batatas-horno-miel-canela"},
    {"ingredients": ["pimientos", "arroz", "carne molida"], "recipe": "Pimientos rellenos de arroz y carne.", "link": "https://example.com/pimientos-rellenos-arroz-carne"},
    {"ingredients": ["quinoa", "espinacas", "aguacate"], "recipe": "Ensalada de quinoa con espinacas y aguacate.", "link": "https://example.com/ensalada-quinoa-espinacas-aguacate"},
    {"ingredients": ["bacalao", "patata", "perejil"], "recipe": "Bacalao con patatas y perejil.", "link": "https://example.com/bacalao-patatas-perejil"},
        {"ingredients": ["pollo", "limón", "romero"], "recipe": "Pollo al horno con limón y romero.", "link": "https://example.com/pollo-limon-romero"},
    {"ingredients": ["arroz", "coco", "mango"], "recipe": "Arroz con coco y mango.", "link": "https://example.com/arroz-coco-mango"},
    {"ingredients": ["berenjena", "queso", "salsa de tomate"], "recipe": "Berenjena a la parmesana.", "link": "https://example.com/berenjena-parmesana"},
    {"ingredients": ["huevo", "tomate", "espinacas"], "recipe": "Frittata de espinacas y tomate.", "link": "https://example.com/frittata-espinacas-tomate"},
    {"ingredients": ["papa", "tocino", "queso"], "recipe": "Papas gratinadas con tocino y queso.", "link": "https://example.com/papas-gratinadas-tocino-queso"},
    {"ingredients": ["zanahoria", "miel", "romero"], "recipe": "Zanahorias al horno con miel y romero.", "link": "https://example.com/zanahorias-horno-miel-romero"},
    {"ingredients": ["pollo", "soja", "sésamo"], "recipe": "Pollo teriyaki con semillas de sésamo.", "link": "https://example.com/pollo-teriyaki-sesamo"},
    {"ingredients": ["calabaza", "cebolla", "ajo"], "recipe": "Sopa de calabaza y cebolla.", "link": "https://example.com/sopa-calabaza-cebolla"},
    {"ingredients": ["quinoa", "zanahoria", "guisantes"], "recipe": "Salteado de quinoa con zanahorias y guisantes.", "link": "https://example.com/salteado-quinoa-zanahorias-guisantes"},
    {"ingredients": ["espaguetis", "ajo", "aceite de oliva"], "recipe": "Espaguetis al aglio e olio.", "link": "https://example.com/espaguetis-aglio-e-olio"},
    {"ingredients": ["manzana", "pasas", "canela"], "recipe": "Manzanas horneadas con pasas y canela.", "link": "https://example.com/manzanas-horneadas-pasas-canela"},
    {"ingredients": ["pollo", "pimientos", "piña"], "recipe": "Pollo agridulce con piña.", "link": "https://example.com/pollo-agridulce-pina"},
    {"ingredients": ["brócoli", "queso cheddar", "leche"], "recipe": "Sopa cremosa de brócoli con queso cheddar.", "link": "https://example.com/sopa-brocoli-cheddar"},
    {"ingredients": ["salmón", "soja", "miel"], "recipe": "Salmón glaseado con soja y miel.", "link": "https://example.com/salmon-glaseado-soja-miel"},
    {"ingredients": ["arroz", "azafrán", "mariscos"], "recipe": "Paella de mariscos.", "link": "https://example.com/paella-mariscos"},
    {"ingredients": ["lentejas", "zanahoria", "chorizo"], "recipe": "Guiso de lentejas con zanahoria y chorizo.", "link": "https://example.com/guiso-lentejas-zanahoria-chorizo"},
    {"ingredients": ["tomate", "mozzarella", "albahaca"], "recipe": "Ensalada caprese.", "link": "https://example.com/ensalada-caprese"},
    {"ingredients": ["pollo", "mango", "curry"], "recipe": "Pollo al curry con mango.", "link": "https://example.com/pollo-curry-mango"},
    {"ingredients": ["calabacín", "pimiento", "quinoa"], "recipe": "Calabacines rellenos de quinoa y pimientos.", "link": "https://example.com/calabacines-rellenos-quinoa-pimientos"},
    {"ingredients": ["tofu", "soja", "jengibre"], "recipe": "Tofu salteado con soja y jengibre.", "link": "https://example.com/tofu-salteado-soja-jengibre"},
    {"ingredients": ["champiñones", "ajo", "vino blanco"], "recipe": "Champiñones al ajillo con vino blanco.", "link": "https://example.com/champinones-ajillo-vino-blanco"},
    {"ingredients": ["huevo", "papa", "cebolla"], "recipe": "Tortilla española.", "link": "https://example.com/tortilla-espanola"},
    {"ingredients": ["espárragos", "queso parmesano", "mantequilla"], "recipe": "Espárragos al horno con queso parmesano.", "link": "https://example.com/esparragos-horno-queso-parmesano"},
    {"ingredients": ["camote", "miel", "canela"], "recipe": "Camotes al horno con miel y canela.", "link": "https://example.com/camotes-horno-miel-canela"},
    {"ingredients": ["pollo", "ajo", "pimentón"], "recipe": "Pollo al ajillo con pimentón.", "link": "https://example.com/pollo-ajillo-pimenton"},
    {"ingredients": ["arroz", "frijoles", "plátano"], "recipe": "Casado costarricense.", "link": "https://example.com/casado-costarricense"},
    {"ingredients": ["berenjena", "queso ricotta", "espinacas"], "recipe": "Lasaña de berenjenas con ricotta.", "link": "https://example.com/lasana-berenjenas-ricotta"},
    {"ingredients": ["fresas", "yogur", "miel"], "recipe": "Parfait de fresas con yogur.", "link": "https://example.com/parfait-fresas-yogur"},
    {"ingredients": ["huevo", "aguacate", "pan"], "recipe": "Tostada de aguacate con huevo poché.", "link": "https://example.com/tostada-aguacate-huevo"},
    {"ingredients": ["pechuga de pollo", "queso", "jamón"], "recipe": "Cordon bleu de pollo.", "link": "https://example.com/cordon-bleu-pollo"},
    {"ingredients": ["pepino", "yogur", "eneldo"], "recipe": "Ensalada de pepino con yogur y eneldo.", "link": "https://example.com/ensalada-pepino-yogur-eneldo"},
    {"ingredients": ["arroz", "pollo", "guisantes"], "recipe": "Arroz con pollo tradicional.", "link": "https://example.com/arroz-con-pollo"},
    {"ingredients": ["pollo", "mantequilla", "nuez moscada"], "recipe": "Pollo a la mantequilla.", "link": "https://example.com/pollo-mantequilla"},
    {"ingredients": ["pasta", "salsa de queso", "jamón"], "recipe": "Macarrones con queso y jamón.", "link": "https://example.com/macarrones-queso-jamon"},
    {"ingredients": ["pollo", "almendras", "miel"], "recipe": "Pollo con almendras y miel.", "link": "https://example.com/pollo-almendras-miel"},
    {"ingredients": ["guisantes", "menta", "crema"], "recipe": "Sopa cremosa de guisantes con menta.", "link": "https://example.com/sopa-guisantes-menta"},
    {"ingredients": ["pollo", "coco", "curry"], "recipe": "Pollo al curry con coco.", "link": "https://example.com/pollo-curry-coco"},
    {"ingredients": ["atún", "pasta", "mayonesa"], "recipe": "Ensalada de pasta con atún.", "link": "https://example.com/ensalada-pasta-atun"},
    {"ingredients": ["calabacín", "zanahoria", "ajo"], "recipe": "Tallarines de calabacín con zanahoria.", "link": "https://example.com/tallarines-calabacin-zanahoria"},
    {"ingredients": ["queso crema", "salmón", "eneldo"], "recipe": "Rollitos de salmón con queso crema.", "link": "https://example.com/rollitos-salmon-queso-crema"},
    {"ingredients": ["arroz", "pollo", "setas"], "recipe": "Risotto de pollo con setas.", "link": "https://example.com/risotto-pollo-setas"},
    {"ingredients": ["calamares", "ajo", "perejil"], "recipe": "Calamares al ajillo con perejil.", "link": "https://example.com/calamares-ajillo-perejil"},
    {"ingredients": ["chocolate", "leche", "nata"], "recipe": "Mousse de chocolate.", "link": "https://example.com/mousse-chocolate"}
]



def generate_recipe(request):
    if request.method == "POST":
        ingredient1 = request.POST.get("ingredient1", "").lower()
        ingredient2 = request.POST.get("ingredient2", "").lower()
        ingredient3 = request.POST.get("ingredient3", "").lower()

        # Find a matching recipe
        for recipe in RECIPES:
            if set(recipe["ingredients"]) == {ingredient1, ingredient2, ingredient3}:
                return JsonResponse({"recipe": recipe["recipe"], "link": recipe["link"]})

        return JsonResponse({"error": "No matching recipe found."})
    return JsonResponse({"error": "Invalid request."})
