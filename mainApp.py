from flask import Flask, render_template, request, redirect
import random
import re
import csv

app = Flask(__name__) # creates Flask object with the __name__ attribute (which is __main__)





#Kate's Globals
jokeList = ["http://www.laughfactory.com/jokes/clean-jokes ", "http://www.laughfactory.com/jokes/joke-of-the-day", "http://www.laughfactory.com/jokes/latest-jokes", "https://www.buzzfeed.com/jessicamisener/21-jokes-so-stupid-theyre-actually-funny?utm_term=.rvJwzplyw#.sfEXnvx1X",  "http://www.ducksters.com/jokes/knockknock.php"]
videoList = ["https://www.youtube.com/watch?v=XyNlqQId-nk","https://www.youtube.com/watch?v=x3eIKSXXncc", "https://www.youtube.com/watch?v=OSgYQl6GZbU","https://www.youtube.com/watch?v=qL0QROnL-JU","https://www.youtube.com/watch?v=btpA9ywjrUE", "https://www.youtube.com/watch?v=2dhl2M6D4bA"]
riddleList = ["http://www.funology.com/riddles/", "http://www.doriddles.com/Riddles/Hard", "https://www.riddles.com/difficult-riddles", "http://www.playbuzz.com/nickps12/hard-riddles", "http://www.lolwot.com/12-incredibly-difficult-riddles-that-will-drive-you-crazy/"]
songList = ["https://www.youtube.com/watch?v=4m48GqaOz90&list=RDQMjb2m2x1rKpU", "https://www.youtube.com/watch?v=fRh_vgS2dFE&list=RDEMxY4vTJ4nihfJFUtQgu2pAA ", "https://www.youtube.com/watch?v=CevxZvSJLk8&list=RDEM9E_ik5ScxhRL1c_HWNxA2A", "https://www.youtube.com/watch?v=e-ORhEE9VVg&list=RDEMb1vAi4rwXXeDlr7NZ68C_w", "https://www.youtube.com/watch?v=PMivT7MJ41M&list=PL55713C70BA91BD6E"]
gameList = ["https://www.coolmath-games.com/0-run", "https://www.coolmath-games.com/0-frizzle-fraz", "http://www.coolmath-games.com/0-papas-pizzeria", "https://www.miniclip.com/games/bubble-trouble/en/", "http://slither.io"]
exerciseList = ["https://www.youtube.com/watch?v=oBu-pQG6sTY", "https://www.youtube.com/watch?v=r8cexmYOknI", "https://www.youtube.com/watch?v=Lu1qJrjxzME", "https://www.youtube.com/watch?v=HRkNfdlm5Qs", "https://www.youtube.com/watch?v=qWy_aOlB45Y"]
factList = ["https://www.thefactsite.com/2011/07/top-100-random-funny-facts.html", "http://www.livin3.com/50-cool-and-weird-fun-facts-that-you-should-know#did%20you%20know", "http://kids.nationalgeographic.com/explore/adventure_pass/weird-but-true/", "http://www.short-funny.com/fun-facts.php", "http://www.short-funny.com/hilarious-jokes.php"]
quoteList = ["https://www.brainyquote.com/quotes/topics/topic_funny.html", "https://www.pinterest.com/explore/funny-quotes/", "http://www.coolfunnyquotes.com", "http://www.rd.com/jokes/funny-quotes/", "https://www.brainyquote.com/quotes/topics/topic_inspirational.html"]
#endif






#Talia
@app.route("/talia") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'formEntry.html', message="")

@app.route('/talia', methods=['POST'])
def processUserInput():
    meals = {"breakfast": {"Mexican": [["Pan Dulces", "http://farm3.static.flickr.com/2386/2169577152_a9e68e3260.jpg?w=240"], ["Beans and Rice", "http://assets.bonappetit.com/photos/57b14d181b33404414976777/16:9/w_1000,c_limit/mare_red_beans_and_rice_h.jpg"], ["Huevos Rancheros", "https://d3cizcpymoenau.cloudfront.net/images/21443/SFS_Huevos_Rancheros-12.jpg"]], "Italian": [["Caffe Latte", "http://www.attibassicafe.com/wp-content/uploads/2013/02/web10.jpg"],["Cornetto Pastry", "https://cdn0.vox-cdn.com/thumbor/n7FtkOBm6-9IjvgZvXOw2vO41SE=/82x0:972x668/1200x800/filters:focal(82x0:972x668)/cdn0.vox-cdn.com/uploads/chorus_image/image/48842719/pastry-cornetti-dina.0.0.jpg"], ["Caffe Latte and a pastry", "https://s3-media4.fl.yelpcdn.com/bphoto/KTuvYbucUPC7GIwS3zNFBg/o.jpg"]], "American": [["Bagel and Cream Cheese", "http://s.eatthis-cdn.com/media/images/ext/792825960/bagel-cream-cheese.jpg"], ["Breakfast Sandwich", "http://assets.bonappetit.com/photos/57acec251b3340441497533d/16:9/w_1000,c_limit/ba-best-breakfast-sandwich.jpg"], ["Full Breakfast", "http://www.teladoiofirenze.it/wp-content/uploads/2013/10/breakfast.jpg"]], "French": [["Croissant", "https://d1alt1wkdk73qo.cloudfront.net/images/guide/89b54c4bea6e4309b4f3fa7f8b192b41/640x478_ac.jpg"], ["Nutella Crepe", "http://www.mezzokilo.it/UserFiles/Image/ricette/big/crepes-nutella-2.jpg"],["Crock Madam", "http://food.fnr.sndimg.com/content/dam/images/food/fullset/2012/2/17/0/GE0305_Croque-Madam-Sandwich_s4x3.jpg.rend.hgtvcom.616.462.jpeg"]]},"lunch": {"Mexican": [["Nachos", "http://www.taylormademarket.com/wp-content/uploads/2013/08/pizza-nachos.jpg"], ["Tacos", "https://static1.squarespace.com/static/536938f0e4b00eb7103b2ce7/53693948e4b0cccc5fa9ab07/547f6a0de4b0a782f71d5496/1417636365794/uno_dos_tacos_carne_asada.jpg"], ["Steak Burrito Bowl", "http://www.culinaryenvy.com/wp-content/uploads/2016/01/burrito-bowl-overhd-1024sq.jpg"]],"Italian": [["Margherita Pizza", "http://www.saveur.com/sites/saveur.com/files/styles/large_1x_/public/images/2015/11/pizza-margherita_2000x1500_toddcoleman.jpg?itok=EST9oig4"], ["Stromboli", "http://www.simplyscratch.com/wp-content/uploads/2014/06/Homemade-Stromboli-l-www.SimplyScratch.com-recipe.jpg"], ["Pasta Carbonara", "http://assets.simplyrecipes.com/wp-content/uploads/2012/02/pasta-carbonara-horiz-a-1200.jpg"]], "American": [["Panini Sandwich", "http://food.fnr.sndimg.com/content/dam/images/food/fullset/2010/8/30/1/FNM_100110-Insert-010_s4x3.jpg.rend.hgtvcom.1280.960.jpeg"], ["Burger and Fries", "http://www.signatureofsoloncc.com/sites/www.signatureofsoloncc.com/files/predefined-images/burger-fries%20%281%29.jpg"],["Nicoise Salad", "http://cdn2.tmbi.com/TOH/Images/Photos/37/1200x1200/Veggie-Nicoise-Salad_exps133577_TH2379797B11_15_7bC_RMS.jpg"]], "French": [["French Onion Soup", "http://www.seriouseats.com/recipes/assets_c/2015/01/20150116-french-onion-soup-vicky-wasik-20-thumb-1500xauto-418068.jpg"],["Escargots Bourguignon", "http://www.saveur.com/sites/saveur.com/files/styles/large_1x_/public/import/2014/images/2010-10/7-SAV1110_bistro_escargots_P.jpg.jpg?itok=-XRFYrn0"],["Blanquette de Veau", "http://sf2.viepratique.fr/wp-content/uploads/sites/2/2013/11/blanquette-de-veau-e1457428254753.jpg"]]},"dinner": {"Mexican": [["Enchiladas", "http://food.fnr.sndimg.com/content/dam/images/food/fullset/2012/10/1/0/WU0308H_simple-perfect-enchiladas_s4x3.jpg.rend.hgtvcom.616.462.jpeg"],["Stuffed Peppers", "http://www.skinnytaste.com/wp-content/uploads/2008/11/turkey-stuffed-peppers-4.jpg"],["Chicken Chimichangas", "http://www.thewickednoodle.com/wp-content/uploads/2014/01/chimis.jpg"]],"Italian": [["Mushroom Risotto","http://www.recipetineats.com/wp-content/uploads/2016/08/Chicken-Mushroom-Risotto_2-680x486.jpg"],["Tagliatelle Ragu", "http://static.economic.bg/news/7/63161/4802.jpg"],["Italian Pork Stew and Polenta" ,"http://www.italianfoodforever.com/wp-content/uploads/2013/10/porkstew1.jpg"]], "American": [["Roasted Chicken and Salad", "http://cdn-image.myrecipes.com/sites/default/files/image/recipes/su/10/06/chicken-arugula-su-x.jpg"],["Steak and Fries","http://www.lovethispic.com/uploaded_images/40617-Steak-And-Fries.png"],["Surf and Turf", "http://food.fnr.sndimg.com/content/dam/images/food/fullset/2010/12/28/4/FNM_010111-WEDinners-007_s4x3.jpg.rend.hgtvcom.616.462.jpeg"]], "French":[["Duck A L'orange", "http://cdn-image.foodandwine.com/sites/default/files/styles/551x551/public/recipe1015-hd-spiced-duck-a-l-orange_0.jpg?itok=wJi2N24z"],["Beef Bourguignon", "http://cf.therecipecritic.com/wp-content/uploads/2016/11/beefstew4-650x975.jpg"],["Mussels", "http://assets.simplyrecipes.com/wp-content/uploads/2012/03/mussels-white-wine-sauce-horiz-a-1200.jpg"]]}}
    meal = request.form['radioMeal'] # breakfast, lunch, or dinner
    cuisine = request.form['radioCuisine'] # American, Mexican, etc.
    cuisineList = meals[meal][cuisine] # list of possible dishes
    mealDescription = cuisineList[int(request.form['radioCost'])] # low (0), medium (1), or expensive (2) item
    myMessage = "You should get" + " " + " " + mealDescription[0] + "!"
    return render_template('formEntry.html',message=myMessage, image= mealDescription[1] ) # use mealDescription[1] for image



#Amina
@app.route("/amina") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'formEntry.html', message="")


@app.route('/amina', methods=['POST'])
def processUserInput():
    carbs = int(request.form['carbs'])
    protein = int(request.form['protein'])
    fat = int(request.form['fat'])

    cpf = carbs + protein + fat

    def switcher(val):
        switch = {
            21: {"carbs":"low","protein":"low","fat":"low",
                    "groceries":{
                        "Spinach","Broccoli","Carrots","Cucumber","Celery", "Romaine lettuce",
                        "Sugar Snap Peas"
                    }
                 },
            22: {"carbs":"high","protein":"low","fat":"low",
                    "groceries":{
                        "Oats", "Brown Rice", "Sweet Potatoes", "Bananas", "Quinoa", "Chickpeas",
                        "Butternut Squash"
                    }
                 },
            25: {"carbs":"low","protein":"high","fat":"low",
                    "groceries":{
                        "Kidney Beans", "Greek Yogurt","Artichoke","Tofu", "Beef"
                    }
                 },
            26: {"carbs":"high","protein":"high","fat":"low",
                    "groceries":{
                        "Sweet Potatoes","Brown Rice","Kidney Beans","Chickpeas","Quinoa","Lentils",
                        "Zucchini"
                    }
                 },
            37: {"carbs":"low","protein":"low","fat":"high",
                    "groceries":{
                        "Avocado","Olive Oil","Buffalo Mozzarella","Coconut Milk",
                        "Chia seeds","Fish","Coconut Oil"
                    }
                 },
            38: {"carbs":"high","protein":"low","fat":"high",
                    "groceries":{
                        "Oats","Brown rice","Sweet Potatoes","Buckwheat","Mango",
                        "Avocado","Olive Oil","Buffalo Mozzarella", "Chia Seeds"
                    }
                 },
            41: {"carbs":"low","protein":"high","fat":"high",
                    "groceries":{
                        "Avocado","Olive Oil","Buffalo Mozzarella",
                        "Full Fat greek yogurt","Eggs","Nuts","Kidney beans",
                        "Tofu","Chia seeds"
                    }
                },
            42: {"carbs":"high","protein":"high","fat":"high",
                    "groceries":{
                        "Eggs ","Nuts","Avocado","Greek yogurt","Fish","Tofu",
                        "Oats","Brown rice","Sweet potatoes","Mango","Kidney beans",
                        "Quinoa","Artichoke"
                    }
                },
        }
        return switch.get(val,"nothing")

    output = switcher(cpf)

    return render_template(
        'grocery.html', c=output["carbs"],p=output["protein"],f=output["fat"], g=output["groceries"])



#grace
@app.route("/grace")
def landingPage():
    return render_template(
        'closetOrganizer.html', message="")

@app.route('/grace', methods=['POST'])
def processUserInput():
    weather = request.form['weather']
    style = request.form['style']
    message = personalStylist(weather, style)
    return render_template(
        'closetOrganizer.html', message=message)

class ClosetItem(object):
    def __init__(self, name, weather, style, isTop):
        self.name = name
        self.weather = weather
        self.style = style
        self.isTop = isTop
        colorChoices = ["a red", "an orange", "a yellow", "a green", "a blue", "a purple", "a black", "a white", "a gray", "a brown", "a pink"]
        self.color = colorChoices[random.randint(0,len(colorChoices)-1)]

    def getItem(self):
        if self.isTop == True:
            item = "top"
        else:
            item = "bottom"
        return self.color + " " + self.name

def personalStylist(weatherChoice, styleChoice):
    cropTop = ClosetItem("crop top", "hot", "casual", True)
    jeanShorts = ClosetItem("pair of jean shorts", "hot", "casual", False)
    dress = ClosetItem("dress", "hot", "fancy", True)
    tankTop = ClosetItem("tank top", "hot", "sporty", True)
    athleticShorts = ClosetItem("pair of athletic shorts", "hot", "sporty", False)
    bigSleepingTee = ClosetItem("big sleeping shirt", "hot", "sleepy", True)
    boxers = ClosetItem("pair of boxers", "hot", "sleepy", False)
    shortSleevedTee = ClosetItem("short sleeved t-shirt", "warm", "casual", True)
    bermudaShorts = ClosetItem("pair of bermuda shorts", "warm", "casual", False)
    blouse = ClosetItem("blouse", "warm", "fancy", True)
    shortSkirt = ClosetItem("short skirt", "warm", "fancy", False)
    athleticTop = ClosetItem("athletic top", "warm", "sporty", True)
    kneeLengthYogaPants = ClosetItem("knee length yoga pants", "warm", "sporty", False)
    shortSleevedPJTop = ClosetItem("short sleeved PJ top", "warm", "sleepy", True)
    pJBottoms = ClosetItem("pair of PJ bottoms", "warm", "sleepy", False)
    longSleevedTee = ClosetItem("long sleeved t-shirt", "chilly", "casual", True)
    jeanPants = ClosetItem("pair of jean pants", "chilly", "casual", False)
    buttonDown = ClosetItem("button down", "chilly", "fancy", True)
    longSkirt = ClosetItem("long skirt", "chilly", "fancy", False)
    sweatshirt = ClosetItem("sweatshirt", "chilly", "sporty", True)
    ankleLengthYogaPants = ClosetItem("pair of ankle length yoga pants", "chilly", "sporty", False)
    longSleevedPJTop = ClosetItem("long sleeved PJ top", "chilly", "sleepy", True)
    sweatpants = ClosetItem("pair of sweatpants", "chilly", "sleepy", False)
    jacket = ClosetItem("jacket", "cold", "casual", True)
    snowPants = ClosetItem("pair of snow pants", "cold", "casual", False)
    coat = ClosetItem("coat", "cold", "fancy", True)
    dressPants = ClosetItem("pair of dress pants", "cold", "fancy", False)
    trackSuit = ClosetItem("track suit", "cold", "sporty", True)
    onesie = ClosetItem("onesie", "cold", "sleepy", True)

    if weatherChoice == "hot" and styleChoice == "casual":
        return "Try " + cropTop.getItem() + " with " + jeanShorts.getItem() + "."
    elif weatherChoice == "hot" and styleChoice == "fancy":
        return "Try " + dress.getItem() + "."
    elif weatherChoice == "hot" and styleChoice == "sporty":
        return "Try " + tankTop.getItem() + " with " + athleticShorts.getItem() + "."
    elif weatherChoice == "hot" and styleChoice == "sleepy":
        return "Try " + bigSleepingTee.getItem() + " with " + boxers.getItem() + "."
    elif weatherChoice == "warm" and styleChoice == "casual":
        return "Try " + shortSleevedTee.getItem() + " with " + bermudaShorts.getItem() + "."
    elif weatherChoice == "warm" and styleChoice == "fancy":
        return "Try " + blouse.getItem() + " with " + shortSkirt.getItem() + "."
    elif weatherChoice == "warm" and styleChoice == "sporty":
        return "Try " + athleticTop.getItem() + " with " + kneeLengthYogaPants.getItem() + "."
    elif weatherChoice == "warm" and styleChoice == "sleepy":
        return "Try " + shortSleevedPJTop.getItem() + " with " + pJBottoms.getItem() + "."
    elif weatherChoice == "chilly" and styleChoice == "casual":
        return "Try " + longSleevedTee.getItem() + " with " + jeanPants.getItem() + "."
    elif weatherChoice == "chilly" and styleChoice == "fancy":
        return "Try " + buttonDown.getItem() + " with " + longSkirt.getItem() + "."
    elif weatherChoice == "chilly" and styleChoice == "sporty":
        return "Try " + sweatshirt.getItem() + " with " + ankleLengthYogaPants.getItem() + "."
    elif weatherChoice == "chilly" and styleChoice == "sleepy":
        return "Try " + longSleevedPJTop.getItem() + " with " + sweatpants.getItem() + "."
    elif weatherChoice == "cold" and styleChoice == "casual":
        return "Try " + jacket.getItem() + " with " + snowPants.getItem() + "."
    elif weatherChoice == "cold" and styleChoice == "fancy":
        return "Try " + coat.getItem() + " with " + dressPants.getItem() + "."
    elif weatherChoice == "cold" and styleChoice == "sporty":
        return "Try " + trackSuit.getItem() + "."
    elif weatherChoice == "cold" and styleChoice == "sleepy":
        return "Try " + onesie.getItem() + "."


#jordan
@app.route("/jordan") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'formEntry.html', message="")

@app.route('/jordan', methods=['POST'])
def processUserInput():
    exercises = {"CARDIO": {"one":["treadmill", "jumping jacks"], "full":["treadmill and high knees", "jumping jacks and high knees"]}, "ABS": {"one":["crunches", "two arm plank"], "full":["bosu crunches and jump lunges", "two arm planks and "]}, "STRENGTH": {"one":["treadmill", "jumping jacks"], "full":["treadmill", "jumping jacks"]}}
    submitButton = request.form["my-form"]
    if submitButton == "GIVE ME MY WORKOUT!":
        exerciseType = request.form['type']
        exerciseWorkoutType = request.form['radioWorkoutType']
        exerciseEquipment = request.form['radioEquipment']
        exercise = exercises[exerciseType][exerciseWorkoutType][int(exerciseEquipment)]
        myMessage = "Your exercise is to do " + exercise
    else:
        exerciseType = random.choice(['CARDIO', 'ABS', 'STRENGTH'])
        exerciseWorkoutType = random.choice(['one', 'full'])
        exerciseEquipment = random.randint(0,1)
        exercise = exercises[exerciseType][exerciseWorkoutType][exerciseEquipment]
        myMessage = "Your exercise is to do " + exercise


    return render_template(
        'formEntry.html',message=myMessage)



#kate
@app.route("/kate")
def landingPage():
    return render_template(
        'formEntry.html', message="")

@app.route("/kate", methods=['POST']) #formEntry.html
def changePage():
    if request.method == 'POST':
        if request.form["answer"] == "yes":
            return render_template(
                "responseScreen.html")
        elif request.form["answer"] == "no":
            return render_template(
                "no.html")


@app.route('/kate/responseScreen', methods=['POST'])
def processUserInput():
    if request.method == 'POST':
        category = request.form['buttonChoices']
        URL= pickLink(category)
        return redirect(URL)


def pickLink(category):
    if category == "joke":
        return jokeList[random.randint(0,len(jokeList)-1)]
    elif category == "video":
            return videoList[random.randint(0,len(videoList)-1)]
    elif category == "riddle":
            return riddleList[random.randint(0,len(riddleList)-1)]
    elif category == "song":
            return songList[random.randint(0,len(songList)-1)]
    elif category == "game":
            return gameList[random.randint(0,len(gameList)-1)]
    elif category == "exercise":
            return exerciseList[random.randint(0,len(exerciseList)-1)]
    elif category == "fact":
            return factList[random.randint(0,len(factList)-1)]
    elif category == "quote":
        return quoteList[random.randint(0,len(quoteList)-1)]
    else:
        return "error"



#LaurenA
@app.route("/laurena") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'FinalHTML.html', feedback="", tip="")

@app.route('/laurena', methods=['POST'])
def processUserInput():
    gender = request.form['gender']
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    age = int(request.form['age'])
    calories = int(request.form['ate'])
    if "gender"=="Male":
        x=calories - (66.47+ (13.75*(weight/2.2)) + (5.0*height*2.54) - (6.75*age))
    else:
        x=calories -(665.09 + (9.56*(weight/2.2)) + (1.84*height*2.54) - (4.67*age))
    tip=""
    if x>-20 and x<20:
        tip="You are just right. Keep up the great work!"
    elif x<-21 and x>-200:
        tip="Your are under have a quick snack"
    elif x<-201:
        tip="Your are under have a meal to keep a good balanced lifestyle"
    elif x>21 and x<80:
        tip="Try to do 20 jumping jacks to kill some calories and get the blood moving"
    elif x>81 and x<130:
        tip="Try to do 20 rowboats and plank for one minute"
    elif x>131:
        tip="I recommend a workout and drinking more water. Also next time you get hungry try watermelon, it is both delicious and healthy"


    return render_template('FinalHTML.html',feedback=x,tip=tip)




#LaurenT
def to_words(text):
    return re.findall(r'\w+', text)

@app.route("/laurent") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'formEntry.html', message="")

@app.route('/laurent', methods=['POST'])


def processUserInput():
    n1 = str(request.form['n1'])
    n2 = str(request.form['n2'])
    addA = ""
    addB = ""
    for i in range(len(to_words(n1))):
        addA = addA + (to_words(n1)[i])[1:] + (to_words(n1)[i])[0] + "ay "
    n1 = addA

    for i in range(len(to_words(n2))):
        addB = addB + (to_words(n2)[i])[-3] + (to_words(n2)[i])[:-3]
    n2 = addB
    total = n1 + n2
    myMessage = " " + str(total)
    return render_template(
        'responseScreen.html',message=myMessage)



#Madeline
@app.route("/madeline") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'formEntry.html', message="")

@app.route('/madeline/formEntry', methods=['POST'])
def processUserInput():
    reaction = request.form['radioKey']

    if reaction == "sharps":
        return render_template(
            'sharpsResponse.html')
    elif reaction == "flats":
        return render_template(
            'flatsResponse.html')
    elif reaction == "none":
        return render_template(
            'noneResponse.html')
    elif reaction == "unsure":
        return render_template(
            "unsureResponse.html")

@app.route("/madeline/sharpsResponse", methods=['POST']) # makes landingPage() execute when you navigate to root directory of local host
def sharpsPage():
    sharpsQuantity = request.form['quantity']
    message1 = "Your piece of music is in the key of G major! The key of G major has " + sharpsQuantity + " sharp and its relative minor is E minor."
    message2 = "Your piece of music is in the key of D major! The key of D major has " + sharpsQuantity + " sharps and its relative minor is B minor."
    message3 = "Your piece of music is in the key of A major! The key of A major has " + sharpsQuantity + " sharps and its relative minor is F sharp minor."
    message4 = "Your piece of music is in the key of E major! The key of E major has " + sharpsQuantity + " sharps and its relative minor is C sharp minor."
    message5 = "Your piece of music is in the key of B major! THe key of B major has " + sharpsQuantity + " sharps and its relative minor is G sharp minor."
    message6 = "Your piece of music is in the key of F sharp major! The key of F sharp major has " + sharpsQuantity + " sharps and its relative minor is D sharp minor."
    message7 = "Your piece of music is in the key of C sharp major! The key of C sharp major has " + sharpsQuantity + " sharps and its relative minor is A sharp minor."
    if sharpsQuantity == "1":
        return render_template('madeline/templates/responseScreen.html', message = message1)
    elif sharpsQuantity == "2":
        return render_template('madeline/templates/responseScreen.html', message = message2)
    elif sharpsQuantity == "3":
        return render_template('madeline/templates/responseScreen.html', message = message3)
    elif sharpsQuantity == "4":
        return render_template('madeline/templates/responseScreen.html', message = message4)
    elif sharpsQuantity == "5":
        return render_template('madeline/templates/responseScreen.html', message = message5)
    elif sharpsQuantity == "6":
        return render_template('madeline/templates/responseScreen.html', message = message6)
    elif sharpsQuantity == "7":
        return render_template('madeline/templates/responseScreen.html', message = message7)
        #message = "Your piece of music is in the key of G major! Key of G has " + sharpsQuantity + " sharps and it's relative minor is A minor."
       # return render_template('responseScreen.html', message=message)

@app.route("/madeline/flatsResponse", methods=['POST']) # makes landingPage() execute when you navigate to root directory of local host
def flatsPage():
    flatsQuantity = request.form['quantityB']
    message1b = "Your piece of music is in the key of F major! The key of F major has " + flatsQuantity + " flat and its relative minor is D minor."
    message2b = "Your piece of music is in the key of B flat major! The key of B flat major has " + flatsQuantity + " flats and its relative minor is G minor."
    message3b = "Your piece of music is in the key of E flat major! The key of E flat major has " + flatsQuantity + " flats and its relative minor is C minor."
    message4b = "Your piece of music is in the key of A flat major! The key of D flat major has " + flatsQuantity + " flats and its relative minor is F minor."
    message5b = "Your piece of music is in the key of D flat major! The key of D flat major has " + flatsQuantity + " flats and its relative minor is B flat minor."
    message6b = "Your piece of music is in the key of G flat major! The key of G flat major has " + flatsQuantity + " flats and its relative minor is E flat minor."
    message7b = "Your piece of music is in the key of C flat major! The key of C flat major has " + flatsQuantity + " flats and its relative minor is A flat minor."
    if flatsQuantity == "1":
        return render_template('madeline/templates/responseScreen.html', message = message1b)
    elif flatsQuantity == "2":
        return render_template('madeline/templates/responseScreen.html', message = message2b)
    elif flatsQuantity == "3":
        return render_template('madeline/templates/responseScreen.html', message = message3b)
    elif flatsQuantity == "4":
        return render_template('madeline/templates/responseScreen.html', message = message4b)
    elif flatsQuantity == "5":
        return render_template('madeline/templates/responseScreen.html', message = message5b)
    elif flatsQuantity == "6":
        return render_template('madeline/templates/responseScreen.html', message = message6b)
    elif flatsQuantity == "7":
        return render_template('madeline/templates/responseScreen.html', message = message7b)



#Nicole
def processUserInputTest(numberofyears, job, skills, home, BFF, vehicle, magicnumber):
    index = magicnumber % len(numberofyears) - 1
    if index < 0:
        index = len(numberofyears) - 1
    year = numberofyears[index]

    index = magicnumber % len(job) - 1
    if index < 0:
        index = len(job) - 1
    job = job[index]

    index = magicnumber % len(skills) - 1
    if index < 0:
        index = len(skills) - 1
    skill = skills[index]

    index = magicnumber % len(home) - 1
    if index < 0:
        index = len(home) - 1
    home = home[index]

    index = magicnumber % len(BFF) - 1
    if index < 0:
        index = len(BFF) - 1
    BFF = BFF[index]

    index = magicnumber % len(vehicle) - 1
    if index < 0:
        index = len(vehicle) - 1
    vehicle = vehicle[index]

    return "In " + str(year) + " years, you will be a " + str(job) + " because you succeed at " + str(skill) + ", live in " + str(home) + " with your best friend, " + str(BFF) + ", drive around in your " + str(vehicle) + ", and live happily ever after."



@app.route("/nicole") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'nicole/templates/formEntry.html', message="")

@app.route('/nicole', methods=['POST'])
def processUserInput():
    numberofyears = [int(request.form['y0'])] #, int(request.form['y1']), int(request.form['y2']), int(request.form['y3'])]
    job = [request.form['j0']] #, request.form['j1'], request.form['j2'], request.form['j3']]
    skills = [request.form['s0']] #, request.form['s1'], request.form['s2'], request.form['s3']]
    home = [request.form['h0']] #, request.form['h1'], request.form['h2'], request.form['h3']]
    BFF = [request.form['b0']] #, request.form['b1'], request.form['b2'], request.form['b3']]
    vehicle = [request.form['v0']] #, request.form['v1'], request.form['v2'], request.form['v3']]
    magicnumber = int(request.form['quantity'])
    myMessage = processUserInputTest(numberofyears, job, skills, home, BFF, vehicle, magicnumber)

    return render_template('nicole/templates/formEntry.html',message=myMessage)




#Rashi
@app.route("/rashi") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'shosho/templates/formEntry.html')

class Movie(object):
    def __init__(self, title, url, percent, actors, summary):
        self.title = title
        self.url = url
        self.percent = percent
        self.actors = actors
        self.summary = summary

d1 = Movie("The Devil Wears Prada", "https://pmcdeadline2.files.wordpress.com/2017/01/the_devil_wears_prada_poster.jpg", "76%","Meryl Streep, Anne Hathaway, Emily Blunt, Stanley Tucci, Adrian Grenier", "Andy(Anne Hathaway) gets a job as assistant to the renowned fashion designer, Miranda Priestly(Meryl Streep), at Runaway magazine. Andy soon learns that the job is much more demanding than she had anticipated, but she learns a few things about fashion and life in her adventure with Miranda Priestly." )
d2 = Movie("The Proposal" , "http://static.tvgcdn.net/rovi/showcards/movie/297350/thumbs/17023104_1300x1733.jpg", "44%","Sandra Bullock, Ryan Reynolds, Betty White, Mary Steenburgen, Craig T. Nelson" , "Facing deportation, Margaret Tate (Sandra Bullock) forces her assistant, Andrew Paxton (Ryan Reynolds), to mary her. Andrew agrees to mary her, if she comes with him to Alaska to meet his family.")
d3 = Movie("The Pink Panther 2", "http://www.imfdb.org/images/thumb/8/82/TPP2.jpg/300px-TPP2.jpg", "12%" , "Steve Martin, Aishwarya Rai, Jean Reno, Andy Garcia, Emily Mortimer, Alfred Molina, Yuki Matsuzaki", "When a theif steals multiple valuable artifacts from around the world including the precious Pink Panther Diamond, a team of detectives come together to find the culprit.")
d4 = Movie("Inside Out", "http://insideoutfullmovie.net/img/inside-out-movie-box.jpg" , "98%" , "Richard Kind(Bing Bong), Mindy Kaling(Disgust), Kaitlyn Dias(Riley), Phyllis Smith(Sadness), Josh Cooley(Jangles), Amy Poehler(Joy), Bill Hader(Fear)" , "When Riley's family chooses to move to San Francisco, her life is turned upside down. Her emotions (Anger, Fear, Joy, and Sadness) work together to make Riley's transition as easy as possible. The story is told through the eyes of the emotion in Riley's head.")
d5 = Movie("13th" , "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAwMjU5NTAzOF5BMl5BanBnXkFtZTgwMjQwODQxMDI@._V1_UX182_CR0,0,182,268_AL_.jpg" , "23%", "Various Interviewees and former historical figures" ,"This documentary explores the history of racial inequality following the passage of the 13th amendment. In specific, the documentary talks about the disproportionate amount of African Americans in comparison to white people in American Prisons." )
d6 = Movie("Mission:Impossible-Rogue Nation", "https://www.zoom.co.uk/assets/images/0/0/2/1/9/mm00219374.jpg?width=450", "93%", "Tom Cruise, Rebecca Ferguson, Simon Pegg, Jeremy Renner, Simon McBurney, Alec Baldwin, Sean Harris, Ving Rhames" , "After the IMF (Impossible Mission Force) is disbanded by the government, IMF agent Ethan Hunt is forced to defeat the Syndicate, a deadly rogue group of agents, on his own. With the help of his team and a few friends, he works to unravel the Syndicate.")


def getMovieInformation(genre):
    if genre == "Romance":
        return d2
    elif genre == "Comedy":
        return d3
    elif genre == "Action":
        return d6
    elif genre == "Disney":
        return d4
    elif genre == "Drama":
        return d1
    elif genre == "Documentary":
        return d5

@app.route('/rashi', methods=['POST'])
def processUserInput():
    genre = request.form["radioOpt"]
    movie = getMovieInformation(genre)
    return render_template(
        'shosho/templates/movieInformationTemplate.html',title = movie.title, percent = movie.percent, url = movie.url, actors = movie.actors, summary = movie.summary)





#ShoSho
class Question:
    def __init__(self, question, choiceList, typeList):
        self.question = question
        self.choiceList = choiceList
        self.typeList = typeList

def readCSV(filename):
    questionList = []
    count = 0
    with open(filename)as CSVFile:
        csvreader = csv.reader(CSVFile)
        for row in csvreader:
            if count == 0:
                pass
            else:
                print row
                q = Question(row[0],[row[1],row[3],row[5],row[7]],[row[2],row[4],row[6],row[8]])
                questionList.append(q)
            count += 1

    return questionList

def readDoubleResponseCSV(filename, type):
    questionList = []
    count = 0
    with open(filename)as CSVFile:
        csvreader = csv.reader(CSVFile)
        for row in csvreader:
            if count == 0:
                pass
            else:
                if type == "":
                    print row
                    q = Question(row[1],[row[2],row[4]],[row[3],row[5]])
                    questionList.append(q)
                elif type == row[0]:
                    print row
                    q = Question(row[1],[row[2],row[4]],[row[3],row[5]])
                    questionList.append(q)
            count += 1

    return questionList

msg_desc = {
    "Radical": '''Radical feminism is a perspective within feminism that calls for a radical reordering of society in which male supremacy is eliminated in all social and economic contexts.
Radical feminists seek to abolish patriarchy by challenging existing social norms and institutions, rather than through a purely political process. This includes challenging the notion of traditional gender roles, opposing the sexual objectification of women, and raising public awareness about such issues as rape and violence against women.'''
,    "Socialist": '''Feminist sociology observes gender in its relation to power, both at the level of face-to-face interaction and within society  at large. Focuses include sexual orientation, race, economic status, and nationality.
At the core of feminist sociology is the idea of the systematic oppression of women and the historical dominance of men within most societies: 'patriarchy'. Example: Sheryl Sandberg '''
   , "Intersectionalist":'''Intersectionality is a term coined by American civil rights advocate Kimberle Williams Crenshaw to describe overlapping or intersecting social identities and related systems of oppression, domination, or discrimination. Intersectionality is the idea that multiple identities intersect to create a whole that is different from the component identities. ''',
"Cultural": '''Cultural feminism is a term used to criticize the view that there is a "female nature" or "female essence" or related attempts to revalidate attributes ascribed to femaleness. It is also used to describe theories that commend innate differences between women and men.'''
}

@app.route("/shosho") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    questionList = readCSV("FeminismQuiz/Sheet 1-Table 1.csv")
    return render_template(
        'shosho/templates/formEntry.html', message="",questionList=questionList)

def processInputChoice(questionList, responseList):
    personality_type_dict={'r':'Radical','c':"Cultural",'s':"Socialist",'i':"Intersectionalist"}
    personality_type = ""
    personality_typeList = []
    res_dic = {'r': 0, 'c': 0, 's': 0, 'i': 0, }
    for i in range(len(questionList)):
        q_type = questionList[i].typeList[responseList[i]]
        res_dic[q_type] = res_dic[q_type] + 1

    max = 0
    for cat in res_dic:
        if res_dic[cat] > max:
            max = res_dic[cat]
            # personality_type = cat
    personalityTypeResponseList = []
    for cat in res_dic:
        if res_dic[cat] == max:
            personality_typeList.append(cat)
            personalityTypeResponseList.append(personality_type_dict[cat])
    return personalityTypeResponseList

@app.route('/shosho/submit', methods=['POST'])
def processUserInput():

    questionList = readCSV("FeminismQuiz/Sheet 1-Table 1.csv")

    personality_type_dict={'r':'Radical','c':"Cultural",'s':"Socialist",'i':"Intersectionalist"}

    responseList = []
    for i in range(len(questionList)):
        q_value = int(request.form['group' + str(i+1)])-1
        responseList.append(q_value)

    personalityTypeResponseList = processInputChoice(questionList, responseList)


    if len(personalityTypeResponseList) == 1:
        print personalityTypeResponseList[0]

        return render_template(
            'shosho/templates/responseScreen.html',message="You are a " + personalityTypeResponseList[0] + " feminist. Check out the nifty description below to learn:  ", msg_desc=msg_desc[personalityTypeResponseList[0]])

    if len(personalityTypeResponseList) > 1:
        pTypeMsg = ""
        pTypeMsgCode = ""
        cnt = 0
        for pType in personalityTypeResponseList:

            pTypeMsgCode += pType[0].lower()
            pTypeMsg += pType
            if cnt < len(personalityTypeResponseList)-1:
                pTypeMsg += " and "

            cnt += 1
        personalityTypeResponseList.sort()

        questionList = readDoubleResponseCSV("FeminismQuiz/Sheet 2-Table 1.csv","".join(sorted(pTypeMsgCode)))

        return render_template(
            'shosho/templates/formEntryDouble.html', message=pTypeMsg, question=questionList[0])


@app.route('/shosho/submitDouble', methods=['POST'])
def processUserInputDouble():
    questionList = readDoubleResponseCSV("FeminismQuiz/Sheet 2-Table 1.csv", "")
    q = request.form['q1']
    q_value = request.form['group0']
    res_dic = {'r':0,'c':0,'s':0,'i':0,}
    personality_type_dict={'r':'Radical','c':"Cultural",'s':"Socialist",'i':"Intersectionalist"}
    q_type = ""
    for i in range(len(questionList)):
        if q == questionList[i].question:
            q_type = questionList[i].typeList[int(q_value)-1]
            break



    return render_template(
            'shosho/templates/responseScreen.html',message="You are " + personality_type_dict[q_type] + " !!", msg_desc=msg_desc[personality_type_dict[q_type]])




#Sophia
@app.route("/sophia") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'shosho/templates/formEntry.html')

@app.route('/sophia', methods=['POST'])
def processUserInput():
    food = request.form['food']
    meal = request.form['myDropDown']
    if meal == "Entree":
        if food == "choice1":
            return render_template("shosho/templates/tuna.html")
        elif food == "choice2":
            return render_template("shosho/templates/bruschetta.html")
        elif food == "choice3":
            return render_template("shosho/templates/lemonChicken.html")
    elif meal == "Appetizer":
        if food == "choice1":
            return render_template("shosho/templates/spicedOlives.html")
        elif food == "choice2":
            return render_template("shosho/templates/stuffedPeppers.html")
        elif food == "choice3":
            return render_template("shosho/templates/spicedPitaChips.html")
    elif meal == "Dessert":
        if food == "choice1":
            return render_template("shosho/templates/brownies.html")
        elif food == "choice2":
            return render_template("shosho/templates/pumpkinMuffins.html")
        elif food == "choice3":
            return render_template("shosho/templates/lemonBars.html")




#zannie
board = [[".    ", ".    ", ".    ", ".    "], [".    ", ".    ", ".    ", ".    "], [".    ", ".    ", ".    ", ".    "], [".    ", ".    ", ".    ", ".    "]]
computerXCord = random.randint(0, 3)
computerYCord = random.randint(0, 3)

def makeRows(board):
    listOfStrings = []
    for row in board:
        S = ""
        for point in row:
            S = S + point
        listOfStrings = listOfStrings + [S]
    return listOfStrings


def mark(userXGuess, userYGuess, hit):
    global board
    if hit == True:
        board[userYGuess][userXGuess] = "X"
        return board
    else:
        board[userYGuess][userXGuess] = "O"
        return board

def battleship(userXGuess, userYGuess):
    global computerXCord
    global computerYCord
    computerShip = (computerXCord, computerYCord)
    if userXGuess == computerXCord and userYGuess == computerYCord:
        board = makeRows(mark(userXGuess, userYGuess, True))
        return ["You found the computer's ship. You won!", board]
    elif userXGuess == computerXCord:
        board = makeRows(mark(userXGuess, userYGuess, False))
        return ["Hint: you guessed the X-coordinate correctly!", board]
    elif userYGuess == computerYCord:
        board = makeRows(mark(userXGuess, userYGuess, False))
        return ["Hint: you guessed the Y-coordinate correctly!", board]
    else:
        board = makeRows(mark(userXGuess, userYGuess, False))
        return ["Incorrect guess!", board]


@app.route("/zannie") # makes landingPage() execute when you navigate to root directory of local host
def landingPage():
    return render_template(
        'zannie/templates/formEntry.html', message="")

@app.route('/zannie', methods=['POST'])
def processUserInput():
    userXGuess = int(request.form['n1'])
    userYGuess = int(request.form['n2'])
    result = battleship(userXGuess, userYGuess)
    listOfStrings = makeRows(result[1])
    myRowOne = listOfStrings[0]
    myRowTwo = listOfStrings[1]
    myRowThree = listOfStrings[2]
    myRowFour = listOfStrings[3]
    return render_template(
        'zannie/templates/formEntry.html',message=result[0], rowOne=myRowOne, rowTwo=myRowTwo, rowThree=myRowThree, rowFour=myRowFour)




if __name__ == "__main__": # prevents code in this file from running if imported by another Python script
    # starts the development server for Flask and allows users to visit
    # this web application from the local machine by visiting localhost
    app.run()