from guizero import App, Window, PushButton, Box, Text, Picture, TextBox, Combo

candidate1votes = 0
candidate2votes = 0
candidate3votes = 0

candidate_namelist = []
candidate_sloganlist = []
candidate_idealist = []
candidate_genderlist = []
candidate_imageslist = []

def endElection():
    global candidate1votes, candidate2votes, candidate3votes, candidate_namelist,candidate_sloganlist,candidate_idealist,candidate_genderlist,candidate_imageslist

    if candidate1votes > candidate2votes and candidate1votes > candidate3votes:
        winner = candidate_namelist[0]
        winnerVotes = candidate1votes
        candidate_greekcheck = candidate_genderlist[0]
        if candidate_genderlist[0] == "Greek":
            winner = "a stupid Greek so second place won"

        loser1 = candidate_namelist[1]
        loser2 = candidate_namelist[2]

        loser1votes = candidate2votes
        loser2votes = candidate3votes

        if loser1votes>loser2votes:
            secondPlace = loser1
            lastPlace = loser2
            secondPlaceVotes = candidate2votes
            thirdPlaceVotes = candidate3votes
        else:
            secondPlace = loser2
            lastPlace = loser1
            secondPlaceVotes = candidate3votes
            thirdPlaceVotes = candidate2votes

    if candidate2votes > candidate3votes and candidate2votes > candidate1votes:
        winner = candidate_namelist[1]
        winnerVotes = candidate2votes
        candidate_greekcheck = candidate_genderlist[1]
        if candidate_genderlist[1] == "Greek":
            winner = "a stupid Greek so second place won"

        loser1 = candidate_namelist[2]
        loser2 = candidate_namelist[0]

        loser1votes = candidate3votes
        loser2votes = candidate1votes

        if loser1votes>loser2votes:
            secondPlace = loser1
            lastPlace = loser2
            secondPlaceVotes = candidate3votes
            thirdPlaceVotes = candidate1votes
        else:
            secondPlace = loser2
            lastPlace = loser1
            secondPlaceVotes = candidate1votes
            thirdPlaceVotes = candidate3votes

    if candidate3votes > candidate2votes and candidate3votes > candidate1votes:
        winner = candidate_namelist[2]
        winnerVotes = candidate3votes
        candidate_greekcheck = candidate_genderlist[2]
        if candidate_greekcheck == "Greek":
            winner = " a stupid Greek so second place won"

        loser1 = candidate_namelist[1]
        loser2 = candidate_namelist[0]

        loser1votes = candidate2votes
        loser2votes = candidate1votes

        if loser1votes>loser2votes:
            secondPlace = loser1
            lastPlace = loser2
            secondPlaceVotes = candidate2votes
            thirdPlaceVotes = candidate1votes
        else:
            secondPlace = loser2
            lastPlace = loser1
            secondPlaceVotes = candidate1votes
            thirdPlaceVotes = candidate2votes

    if candidate2votes==candidate1votes==candidate3votes:
        winner = "nobody! There was a tie! NO OVERALL WINNER"
        winnerVotes = "A tie"
        secondPlace = "None"
        lastPlace = "None"
        secondPlaceVotes = "Unavailable"
        thirdPlaceVotes = "Unavailable"
    app.info("Winner!", "The winner is " + winner + " with " + str(winnerVotes) +  ". Second place was " + secondPlace + " with " + str(secondPlaceVotes) + ". And in last " + lastPlace + " with " + str(thirdPlaceVotes) + ".")

    candidate1votes = 0
    candidate2votes = 0
    candidate3votes = 0

    candidate_namelist = []
    candidate_sloganlist = []
    candidate_idealist = []
    candidate_genderlist = []
    candidate_imageslist = []

def castVote():
    global candidate1votes, candidate2votes, candidate3votes

    def back_buttonFunc():
        voteWindow.hide()

    def candOneInfo():
        def back_buttonInfo():
            candOneWindow.hide()

        def vote_cast():
            global candidate1votes, candidate2votes, candidate3votes

            if candidate1votes+candidate2votes+candidate3votes >= 30:
                app.info("Uh oh!", "The maximum number of votes have been counted!")
            else:
                candidate1votes = candidate1votes + 1
                voteWindow.hide()
                candOneWindow.hide()

        candOneWindow = Window(voteWindow, width=1428, height=1200, bg = "#27811e")
        mainInfoBox = Box(candOneWindow, width=1450, height=700, border=True, align="bottom")
        back_button = Picture(candOneWindow, width= 65, height = 70, image = "Images/Guizero projects image/backButton.png", align = "left")
        back_button.when_clicked = back_buttonInfo

        candidate_title = Text(candOneWindow, size=50, text=candidate_namelist[0], color = "white", font = "Oswald")

        rightSpacer = Box(mainInfoBox, width = 100, height = 1, align = "right")
        leftBox = Box(mainInfoBox, width = 800, height = 700, align = "left", border = True)
        imageBox = Box(leftBox, width = 100, height = 700, align = "left", border =False)
        traitBox = Box(leftBox, width = 270, height = 700, align = "left", border =False)
        infoBoxGender = Box(leftBox, width = 450, height = 257, align = "top", border =False)
        infoBoxIdeas1 = Box(leftBox, width = 450, height = 100, align = "top", border =False)
        infoBoxIdeas2 = Box(leftBox, width = 450, height = 110, align = "top", border =False)
        infoBoxIdeas3 = Box(leftBox, width = 450, height = 150, align = "top", border =False)

        spacerInfo = Box(mainInfoBox, height= 130, width = 300)
        candidate1picture = Picture(mainInfoBox, width = 290, height = 350, image = candidate_imageslist[0])

        slogan = Text(mainInfoBox, text= "''" + candidate_sloganlist[0] + "''", size = 30, color = "white", font = "Oswald", width = 240)
        signature = Text(mainInfoBox, size = 30, color = "white", font = "Oswald", text = "-" + candidate_namelist[0])

        spacer7 = Box(imageBox, width=1, height = 95)

        voteSpacer = Box(spacerInfo, width = 1, height = 50)
        voteButton = PushButton(spacerInfo, width = 300, command = vote_cast)
        voteButton.text = "Click here to vote for this candidate"

        genderImage = Picture(imageBox, width=75, height=75, image = "Images/Guizero projects image/genderIcon.png")
        spacer8 = Box(traitBox, width=1, height = 100)
        genderText = Text(traitBox, size = 30, text = candidate_namelist[0] + "'s gender: ", color="white", font = "Oswald")
        candGender = Text(infoBoxGender, text = candidate_genderlist[0], color="white", font = "Oswald", size = 30, align = "left")

        spacer9 = Box(imageBox, width=1, height = 90)
        ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")
        spacer11 = Box(imageBox, width=1, height = 30)
        ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")
        spacer12 = Box(imageBox, width=1, height = 30)
        ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")

        spacer10 = Box(traitBox, width=1, height = 145)
        ideasText = Text(traitBox, size = 30, text = candidate_namelist[0] + "'s idea 1: ", color = "white", font = "Oswald")
        spacer13 = Box(traitBox, width=1, height = 80)
        ideasText = Text(traitBox, size = 30, text = candidate_namelist[0] + "'s idea 2: ", color = "white", font = "Oswald")
        spacer14 = Box(traitBox, width=1, height = 90)
        ideasText = Text(traitBox, size = 30, text = candidate_namelist[0] + "'s idea 3: ", color = "white", font = "Oswald")

        spacer15 = Box(infoBoxIdeas1, width=1, height = 40)
        candIdea1 = Text(infoBoxIdeas1, text = candidate_idealist[0], color = "white", font = "Oswald", size = 30, align = "left")
        spacer16 = Box(infoBoxIdeas2, width=1, height = 80)
        candIdea2 = Text(infoBoxIdeas2, text = candidate_idealist[1], color = "white", font = "Oswald", size = 30, align = "left")
        spacer17 = Box(infoBoxIdeas3, width=1, height = 90)
        candIdea3 = Text(infoBoxIdeas3, text = candidate_idealist[2], color = "white", font = "Oswald", size = 30, align = "left")

    def candTwoInfo():
            def back_buttonInfo():
                candOneWindow.hide()

            def vote_cast():
                global candidate1votes, candidate2votes, candidate3votes

                if candidate1votes+candidate2votes+candidate3votes >= 30:
                    app.info("Uh oh!", "The maximum number of votes have been counted!")
                else:
                    candidate2votes = candidate2votes + 1
                    voteWindow.hide()
                    candOneWindow.hide()

            candOneWindow = Window(voteWindow, width=1428, height=1200, bg = "#27811e")
            mainInfoBox = Box(candOneWindow, width=1450, height=700, border=True, align="bottom")
            back_button = Picture(candOneWindow, width= 65, height = 70, image = "Images/Guizero projects image/backButton.png", align = "left")
            back_button.when_clicked = back_buttonInfo

            candidate_title = Text(candOneWindow, size=50, text=candidate_namelist[1], color = "white", font = "Oswald")

            rightSpacer = Box(mainInfoBox, width = 100, height = 1, align = "right")
            leftBox = Box(mainInfoBox, width = 800, height = 700, align = "left", border = True)
            imageBox = Box(leftBox, width = 100, height = 700, align = "left", border =False)
            traitBox = Box(leftBox, width = 270, height = 700, align = "left", border =False)
            infoBoxGender = Box(leftBox, width = 450, height = 257, align = "top", border =False)
            infoBoxIdeas1 = Box(leftBox, width = 450, height = 100, align = "top", border =False)
            infoBoxIdeas2 = Box(leftBox, width = 450, height = 110, align = "top", border =False)
            infoBoxIdeas3 = Box(leftBox, width = 450, height = 150, align = "top", border =False)

            spacerInfo = Box(mainInfoBox, height= 130, width = 300)
            candidate1picture = Picture(mainInfoBox, width = 290, height = 350, image = candidate_imageslist[1])

            slogan = Text(mainInfoBox, text= "''" + candidate_sloganlist[1] + "''", size = 30, color = "white", font = "Oswald", width = 240)
            signature = Text(mainInfoBox, size = 30, color = "white", font = "Oswald", text = "-" + candidate_namelist[1])

            spacer7 = Box(imageBox, width=1, height = 95)

            voteSpacer = Box(spacerInfo, width = 1, height = 50)
            voteButton = PushButton(spacerInfo, width = 300, command = vote_cast)
            voteButton.text = "Click here to vote for this candidate"

            genderImage = Picture(imageBox, width=75, height=75, image = "Images/Guizero projects image/genderIcon.png")
            spacer8 = Box(traitBox, width=1, height = 100)
            genderText = Text(traitBox, size = 30, text = candidate_namelist[1] + "'s gender: ", color="white", font = "Oswald")
            candGender = Text(infoBoxGender, text = candidate_genderlist[1], color="white", font = "Oswald", size = 30, align = "left")

            spacer9 = Box(imageBox, width=1, height = 90)
            ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")
            spacer11 = Box(imageBox, width=1, height = 30)
            ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")
            spacer12 = Box(imageBox, width=1, height = 30)
            ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")

            spacer10 = Box(traitBox, width=1, height = 145)
            ideasText = Text(traitBox, size = 30, text = candidate_namelist[1] + "'s idea 1: ", color = "white", font = "Oswald")
            spacer13 = Box(traitBox, width=1, height = 80)
            ideasText = Text(traitBox, size = 30, text = candidate_namelist[1] + "'s idea 2: ", color = "white", font = "Oswald")
            spacer14 = Box(traitBox, width=1, height = 90)
            ideasText = Text(traitBox, size = 30, text = candidate_namelist[1] + "'s idea 3: ", color = "white", font = "Oswald")

            spacer15 = Box(infoBoxIdeas1, width=1, height = 40)
            candIdea1 = Text(infoBoxIdeas1, text = candidate_idealist[3], color = "white", font = "Oswald", size = 30, align = "left")
            spacer16 = Box(infoBoxIdeas2, width=1, height = 80)
            candIdea2 = Text(infoBoxIdeas2, text = candidate_idealist[4], color = "white", font = "Oswald", size = 30, align = "left")
            spacer17 = Box(infoBoxIdeas3, width=1, height = 90)
            candIdea3 = Text(infoBoxIdeas3, text = candidate_idealist[5], color = "white", font = "Oswald", size = 30, align = "left")

    def candThreeInfo():
            def back_buttonInfo():
                candOneWindow.hide()

            def vote_cast():
                global candidate1votes, candidate2votes, candidate3votes

                if candidate1votes+candidate2votes+candidate3votes >= 30:
                    app.info("Uh oh!", "The maximum number of votes have been counted!")
                else:
                    candidate3votes = candidate3votes + 1
                    voteWindow.hide()
                    candOneWindow.hide()

            candOneWindow = Window(voteWindow, width=1428, height=1200, bg = "#27811e")
            mainInfoBox = Box(candOneWindow, width=1450, height=700, border=True, align="bottom")
            back_button = Picture(candOneWindow, width= 65, height = 70, image = "Images/Guizero projects image/backButton.png", align = "left")
            back_button.when_clicked = back_buttonInfo

            candidate_title = Text(candOneWindow, size=50, text=candidate_namelist[2], color = "white", font = "Oswald")

            rightSpacer = Box(mainInfoBox, width = 100, height = 1, align = "right")
            leftBox = Box(mainInfoBox, width = 800, height = 700, align = "left", border = True)
            imageBox = Box(leftBox, width = 100, height = 700, align = "left", border =False)
            traitBox = Box(leftBox, width = 270, height = 700, align = "left", border =False)
            infoBoxGender = Box(leftBox, width = 450, height = 257, align = "top", border =False)
            infoBoxIdeas1 = Box(leftBox, width = 450, height = 100, align = "top", border =False)
            infoBoxIdeas2 = Box(leftBox, width = 450, height = 110, align = "top", border =False)
            infoBoxIdeas3 = Box(leftBox, width = 450, height = 150, align = "top", border =False)

            spacerInfo = Box(mainInfoBox, height= 130, width = 300)
            candidate1picture = Picture(mainInfoBox, width = 290, height = 350, image = candidate_imageslist[2])

            slogan = Text(mainInfoBox, text= "''" + candidate_sloganlist[2] + "''", size = 30, color = "white", font = "Oswald", width = 240)
            signature = Text(mainInfoBox, size = 30, color = "white", font = "Oswald", text = "-" + candidate_namelist[2])

            spacer7 = Box(imageBox, width=1, height = 95)

            voteSpacer = Box(spacerInfo, width = 1, height = 50)
            voteButton = PushButton(spacerInfo, width = 300, command = vote_cast)
            voteButton.text = "Click here to vote for this candidate"

            genderImage = Picture(imageBox, width=75, height=75, image = "Images/Guizero projects image/genderIcon.png")
            spacer8 = Box(traitBox, width=1, height = 100)
            genderText = Text(traitBox, size = 30, text = candidate_namelist[2] + "'s gender: ", color="white", font = "Oswald")
            candGender = Text(infoBoxGender, text = candidate_genderlist[2], color="white", font = "Oswald", size = 30, align = "left")

            spacer9 = Box(imageBox, width=1, height = 90)
            ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")
            spacer11 = Box(imageBox, width=1, height = 30)
            ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")
            spacer12 = Box(imageBox, width=1, height = 30)
            ideasImage = Picture(imageBox, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")

            spacer10 = Box(traitBox, width=1, height = 145)
            ideasText = Text(traitBox, size = 30, text = candidate_namelist[2] + "'s idea 1: ", color = "white", font = "Oswald")
            spacer13 = Box(traitBox, width=1, height = 80)
            ideasText = Text(traitBox, size = 30, text = candidate_namelist[2] + "'s idea 2: ", color = "white", font = "Oswald")
            spacer14 = Box(traitBox, width=1, height = 90)
            ideasText = Text(traitBox, size = 30, text = candidate_namelist[2] + "'s idea 3: ", color = "white", font = "Oswald")

            spacer15 = Box(infoBoxIdeas1, width=1, height = 40)
            candIdea1 = Text(infoBoxIdeas1, text = candidate_idealist[6], color = "white", font = "Oswald", size = 30, align = "left")
            spacer16 = Box(infoBoxIdeas2, width=1, height = 80)
            candIdea2 = Text(infoBoxIdeas2, text = candidate_idealist[7], color = "white", font = "Oswald", size = 30, align = "left")
            spacer17 = Box(infoBoxIdeas3, width=1, height = 90)
            candIdea3 = Text(infoBoxIdeas3, text = candidate_idealist[8], color = "white", font = "Oswald", size = 30, align = "left")

    voteWindow = Window(app, width=1428, height=1200, bg = "#27811e")
    mainBox = Box(voteWindow, width=1450, height=700, border=True, align="bottom")
    back_button = Picture(voteWindow, width= 65, height = 70, image = "Images/Guizero projects image/backButton.png", align = "left")
    back_button.when_clicked = back_buttonFunc
    title3 = Text(voteWindow, size=50, text="Cast Your Vote", color="white", font = "Oswald")

    box1 = Box(mainBox,width =150, height=700, align="left")
    box2 = Box(mainBox,width =290, height=700, align="left")
    box3 = Box(mainBox,width =75, height=700, align="left")
    box4 = Box(mainBox,width =75, height=700, align="left")
    box5 = Box(mainBox,width =290, height=700, align="left")
    box6 = Box(mainBox,width =75, height=700, align="left")
    box7 = Box(mainBox,width =75, height=700, align="left")
    box8 = Box(mainBox,width =290, height=700, align="left")
    box9 = Box(mainBox,width =100, height=700, align="left")

    candidate1picture = Picture(box2, width = 290, height = 350, image = candidate_imageslist[0])
    candidate1name = Text(box2, size=25, text = "1# " + candidate_namelist[0], color = "white", font = "Oswald")

    candidate2picture = Picture(box5, width = 290, height = 350, image = candidate_imageslist[1])
    candidate2name = Text(box5, size=25, text="2# " + candidate_namelist[1], color = "white", font = "Oswald")

    candidate3picture = Picture(box8, width = 290, height = 350, image = candidate_imageslist[2])
    candidate3name = Text(box8, size=25, text="#3 " + candidate_namelist[2], color = "white", font = "Oswald")

    spacer2 = Box(box2, width = 1, height = 35)
    candidate1infoButton = PushButton(box2, width = 15, command = candOneInfo)
    candidate1infoButton.text = "View Info"
    cand1votes = Text(box2, text = "Current votes: " + str(candidate1votes))

    spacerGalanos = Box(box5, width = 1, height = 35)
    candidate2infoButton = PushButton(box5, width = 15, command = candTwoInfo)
    candidate2infoButton.text = "View Info"
    cand2votes = Text(box5, text = "Current votes: " + str(candidate2votes))

    spacerKluck = Box(box8, width = 1, height = 35)
    candidate3infoButton = PushButton(box8, width = 15, command = candThreeInfo)
    candidate3infoButton.text = "View Info"
    cand3votes = Text(box8, text = "Current votes: " + str(candidate3votes))

def addCand():

    def back_buttonFunc():
        addWindow.hide()
    def add_custom_image():
        addWindow.hide()
        user_image=(app.select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=False, filename=""))

        addWindow.show()

        candPhoto.image = user_image
    def save_data():

        candidate_namelist.append(enterName.value)
        candidate_sloganlist.append(enterSlogan.value)
        candidate_genderlist.append(enterGender.value)
        candidate_idealist.append(enterIdeas1.value)
        candidate_idealist.append(enterIdeas2.value)
        candidate_idealist.append(enterIdeas3.value)
        candidate_imageslist.append(candPhoto.image)

        addWindow.destroy()

    if len(candidate_namelist)>=3:
        app.info("Uh oh!", "The max number of candidates have been added! Try next election")
    else:
        addWindow = Window(app, width=1428, height=1200, bg = "#27811e")
        mainBox = Box(addWindow, width=1450, height=700, border=True, align="bottom")
        back_button = Picture(addWindow, width= 65, height = 70, image = "Images/Guizero projects image/backButton.png", align = "left")
        back_button.when_clicked = back_buttonFunc

        box1 = Box(mainBox,width =145, height=700, border=False, align="left")
        box2 = Box(mainBox,width =290, height=700, border=False, align="left")
        box3 = Box(mainBox,width =145, height=700, border=False, align="left")

        space1 = Box(box1, height=10)
        nameImage = Picture(box1, width=75, height=75, image = "Images/Guizero projects image/nameIcon.png")

        space2 = Box(box2, height=30)
        nameText = Text(box2, size = 30, text="Enter Candidate's name: ", color="white", font = "Oswald")

        space3 = Box(box3, height=47)
        enterName = TextBox(box3, width=35)

        spacer4 = Box(box1, width=1, height = 20)
        sloganImage = Picture(box1, width=100, height=100, image = "Images/Guizero projects image/sloganIcon.png")

        spacer5 = Box(box2, width=1, height = 60)
        sloganText = Text(box2, size = 30, text = "Enter candidate's slogan: ", color="white", font = "Oswald")

        spacer6 = Box(box3, width=1, height = 82)
        enterSlogan = TextBox(box3, width = 35)

        spacer7 = Box(box1, width=1, height = 35)
        genderImage = Picture(box1, width=75, height=75, image = "Images/Guizero projects image/genderIcon.png")

        spacer8 = Box(box2, width=1, height = 60)
        genderText = Text(box2, size = 30, text = "Enter candidate's gender: ", color="white", font = "Oswald")

        spacer9 = Box(box3, width=1, height=85)
        enterGender = Combo(box3, width=50 ,options=["Male", "Female", "Other", "Greek"])

        spacer10 = Box(box1, width=1, height=30)
        ideasImage = Picture(box1, width=100, height=100, image = "Images/Guizero projects image/ideaIcon.png")

        spacer11 = Box(box2, width=1, height=80)
        ideasText = Text(box2, size = 30, text = "Enter candidates ideas: ", color = "white", font = "Oswald")

        spacer12 = Box(box3, width=1, height=107)
        enterIdeas1 = TextBox(box3, width = 35)

        spacer13 = Box(box3, width=1, height=50)
        enterIdeas2 = TextBox(box3, width = 35)

        spacer14 = Box(box3, width=1, height=50)
        enterIdeas3 = TextBox(box3, width = 35)

        candSpacer = Box(mainBox, width = 1, height = 50)
        candPhoto=Picture(mainBox, width = 500, height = 600, image = "Images/Guizero projects image/addPhoto.png")
        candPhoto.when_clicked = add_custom_image

        save_button = Picture(addWindow, width = 65, height = 70, image = "Images/Guizero projects image/saveData.png", align = "right")
        title2=Text(addWindow, size=50, text="Add new candidate", color="white", font = "Oswald")
        save_button.when_clicked = save_data

def menu():
    box1 = Box(app, width=714, height=1200, border=True, align="left")
    boxoverlap = Box(app, width=714, height=1200, border=True, align="left")

    titlebox = Box(box1, width=600, height=100, border=False)

    titlespacer=Box(titlebox, height=10)
    title=Text(titlebox, text="Class Captain Voter", size=50, color="white", font = "Oswald")

    box0 = Box(box1, width=200, height=650, border=False, align = "left")
    box3 = Box(box1, width=200, height=650, border=False, align = "right")

    button_spacer1=Box(box1, height=50)

    cast_vote_button = PushButton(box1, align="top", width=15, command = castVote)
    cast_vote_button.text = "   Cast  Vote   "

    button_spacer2=Box(box1, height=50)

    add_cand_button = PushButton(box1, align="top", width=15, command = addCand)
    add_cand_button.text = "Add candidate"

    button_spacer3=Box(box1, height=50)

    old_results_button = PushButton(box1, align="top", width=15)
    old_results_button.text = "View previous results"

    button_spacer4=Box(box1, height=50)

    end_election_button = PushButton(box1, align="top", width=15, command = endElection)
    end_election_button.text = "End election"

    menuVotingImage = Picture(boxoverlap, image="Images/Guizero projects image/HandVoting8.png", height=350, width=350)

    spacer1 = Box(box3, height=20)
    castVoteIcon=Picture(box3, image="Images/Guizero projects image/votingBox5.png", height=80, width=80)

    spacer2 = Box(box3, height=25)
    addCandIcon=Picture(box3, image="Images/Guizero projects image/addCand.png", height=80, width=80)

    spacer3 = Box(box3, height=20)
    previousIcon=Picture(box3, image="Images/Guizero projects image/previousElect2.png", height=80, width=120)

    spacer3 = Box(box3, height=10)
    finishIcon=Picture(box3, image="Images/Guizero projects image/finishElect.png", height=150, width=100)

    app.show

app = App(bg = "#27811e", width=1428, height=1200, )

menu()

app.display()
