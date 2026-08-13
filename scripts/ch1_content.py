from html_i18n import box, h2, h3, h4, img, li_items, nested_ul, p, quote, t, table


IMG = "https://afs-fc-eudeux.systime.dk/fileadmin/"


def body() -> str:
    return "\n".join(
        [
            intro(),
            s11(),
            s12(),
            s13(),
            s14(),
            s15(),
            s16(),
            s17(),
            s18(),
        ]
    )


def intro() -> str:
    return "\n".join(
        [
            p(
                "Virksomheder har altid haft fokus på, hvordan de skaber omsætning og overskud. Grundtanken er enkel:",
                "Companies have always focused on how they create revenue and profit. The basic idea is simple:",
            ),
            quote(
                "Giv kunden værdi – og tjen penge på det",
                "Give the customer value – and make money from it",
            ),
            p("I dette kapitel ser vi på:", "In this chapter we look at:"),
            li_items(
                [
                    (
                        f"Hvad en <span class='term'>forretningsmodel</span> er",
                        f"What a <span class='term'>business model</span> is",
                    ),
                    (
                        "Eksempler på traditionelle (offline) og digitale (online) forretningsmodeller",
                        "Examples of traditional (offline) and digital (online) business models",
                    ),
                    (
                        "Hvordan modellen påvirker valg af kunder og samarbejdspartnere",
                        "How the model affects the choice of customers and partners",
                    ),
                ]
            ),
            img(
                IMG + "_processed_/e/5/csm_221_logoer_ikea_TGTG_airtox_7b9b29e776.jpg",
                "Casevirksomheder: IKEA, Too Good To Go og Airtox",
                "Case companies: IKEA, Too Good To Go and Airtox",
            ),
            p(
                "Du skal arbejde med tre virksomheder med meget forskellige forretningskoncepter:",
                "You will work with three companies that have very different business concepts:",
            ),
            li_items(
                [
                    (
                        f"IKEA – international <span class='term'>handelsvirksomhed</span>, som også designer sine egne produkter",
                        f"IKEA – an international <span class='term'>trading company</span> that also designs its own products",
                    ),
                    (
                        "Airtox – dansk virksomhed, der producerer sikkerhedssko",
                        "Airtox – a Danish company that manufactures safety shoes",
                    ),
                    (
                        "Too Good To Go – digital platform, der hjælper med at sælge overskudsmad",
                        "Too Good To Go – a digital platform that helps sell surplus food",
                    ),
                ]
            ),
            p(
                "Du møder dem gennem case-aktiviteter, så du får viden om:",
                "You will meet them through case activities, so you learn:",
            ),
            li_items(
                [
                    ("Hvordan koncepterne er bygget op", "How the concepts are structured"),
                    ("Hvorfor de adskiller sig fra hinanden", "Why they differ from each other"),
                ]
            ),
            box(
                "exercise",
                "Gruppe-aktivitet",
                "Group activity",
                "\n".join(
                    [
                        h3("Få indsigt i casevirksomhederne", "Get to know the case companies"),
                        p("I skal arbejde i grupper.", "You will work in groups."),
                        p(
                            "Fordel de tre casevirksomheder mellem jer:",
                            "Share the three case companies between you:",
                        ),
                        li_items(
                            [
                                ("IKEA", "IKEA"),
                                ("Airtox B2B", "Airtox B2B"),
                                ("Too Good To Go", "Too Good To Go"),
                            ]
                        ),
                        p(
                            "Forberedelser til fremlæggelse af din casevirksomhed:",
                            "Prepare to present your case company:",
                        ),
                        li_items(
                            [
                                (
                                    "Læs casebeskrivelsen om virksomheden",
                                    "Read the case description of the company",
                                ),
                                (
                                    "Skriv 5 stikord, som siger noget om casevirksomheden",
                                    "Write 5 keywords that say something about the case company",
                                ),
                            ]
                        ),
                        p("Fremlæggelse for din gruppe:", "Present to your group:"),
                        li_items(
                            [
                                (
                                    "Du fremlægger din casevirksomhed ud fra dine stikord",
                                    "You present your case company based on your keywords",
                                ),
                                (
                                    "Herefter diskuterer du din casevirksomhed med gruppen",
                                    "Then you discuss your case company with the group",
                                ),
                            ]
                        ),
                    ]
                ),
            ),
            h3("Sådan er kapitlet bygget op", "How this chapter is structured"),
            h4("Teori og praktiske eksempler", "Theory and practical examples"),
            p(
                "Kapitlets temaer gennemgås med en kort præsentation af teoretiske begreber, værktøjer og modeller. Disse sammenkobles med praktiske eksempler fra virksomheder.",
                "The chapter themes are presented with a short introduction to theoretical concepts, tools and models. These are linked to practical examples from companies.",
            ),
            p(
                "Herefter arbejder eleverne praktisk med case-aktiviteter og opgaver.",
                "Afterwards, students work practically with case activities and exercises.",
            ),
            table(
                [("Læringsaktiviteter", "Learning activities"), ("Værktøj", "Tool")],
                [
                    [
                        ("Lærer introducerer kapitel 1", "The teacher introduces chapter 1"),
                        ("Bogens teori og praktiske eksempler", "The book’s theory and practical examples"),
                    ],
                    [
                        ("Gruppe-aktivitet", "Group activity"),
                        ("Få indsigt i casevirksomhederne", "Get to know the case companies"),
                    ],
                ],
            ),
            h4("Case-aktiviteter og opgaver", "Case activities and exercises"),
            p(
                "Case-aktiviteter er et gennemgående læringselement, som løbende skal bringe elevernes praktiske forståelse for kapitlets temaer i spil. Disse indgår som par-aktivitet eller gruppe-aktivitet.",
                "Case activities are a recurring learning element that continually brings students’ practical understanding of the chapter themes into play. They are done as pair work or group work.",
            ),
            p(
                "Herudover arbejder eleverne med opgaver, der udvælges af læreren efter behov.",
                "In addition, students work with exercises selected by the teacher as needed.",
            ),
            p(
                "Kapitlet indeholder opgaver, der træner begreber, samt større casebaserede opgaver, som går på tværs af kapitlets temaer.",
                "The chapter contains exercises that train key terms, as well as larger case-based assignments that cut across the chapter themes.",
            ),
            h4("Træning og repetition", "Practice and revision"),
            p(
                "Når alle kapitlets temaer er bearbejdet, kan eleverne træne og repetere:",
                "When all of the chapter themes have been covered, students can practise and revise:",
            ),
            li_items(
                [
                    ("Kapitlets vigtigste fagbegreber", "The chapter’s most important terms"),
                    ("5 skarpe til kapitlet", "5 sharp questions on the chapter"),
                    (
                        "En analog træningsopgave med begrebskort",
                        "An analogue practice task with term cards",
                    ),
                ]
            ),
        ]
    )


def s11() -> str:
    return "\n".join(
        [
            h2("s11", "1.1 En forretningsmodel", "1.1 A business model"),
            p(
                "Der findes mange forskellige forretningsmodeller. De kan opdeles ud fra en række fællestræk, som skaber overordnede forretningsmodeller. Det giver et bedre overblik.",
                "There are many different business models. They can be grouped by shared features into broader types of business model. That gives a clearer overview.",
            ),
            h3("Forretningsmodel", "Business model"),
            p(
                "En forretningsmodel er en beskrivelse af den metode, en virksomhed har valgt at tjene penge på.",
                "A business model is a description of the method a company has chosen to make money.",
            ),
            p(
                "Det er en beskrivelse af, hvilken værdi virksomheden skaber, hvordan værdien skabes, samt hvordan det gøres interessant for kunden.",
                "It describes what value the company creates, how that value is created, and how it is made attractive to the customer.",
            ),
            p(
                "Alle virksomheder bygger på en forretningsmodel.",
                "Every company is built on a business model.",
            ),
            p(
                "Dette gælder både for virksomheder, der har fokus på at tjene penge i den fysiske verden, fx Salling Group, og også for virksomheder, der har fokus på at tjene penge i den digitale verden, fx Spotify.",
                "This applies both to companies that make money in the physical world, for example Salling Group, and to companies that make money in the digital world, for example Spotify.",
            ),
            p(
                "Modellen herunder viser de grundlæggende byggesten eller elementer, som en forretningsmodel består af.",
                "The model below shows the basic building blocks, or elements, that a business model consists of.",
            ),
            img(
                IMG + "_processed_/3/8/csm_218_Byggesten_forretningsmodel_9a8f913ac8.png",
                "Byggesten i en forretningsmodel",
                "Building blocks of a business model",
            ),
            h3("Kendetegn ved forretningsmodellen", "Features of the business model"),
            li_items(
                [
                    (
                        f"<strong>Værditilbud:</strong> Skaber og leverer et produkt eller en <span class='term'>serviceydelse</span>, der har værdi for kunderne",
                        f"<strong>Value proposition:</strong> Creates and delivers a product or <span class='term'>service</span> that has value for customers",
                    ),
                    (
                        "<strong>Kunder:</strong> Kender sin kunde og kundens årsag til at købe produktet eller serviceydelsen",
                        "<strong>Customers:</strong> Knows its customer and the customer’s reason for buying the product or service",
                    ),
                    (
                        "<strong>Samarbejdspartnere:</strong> Involverer de samarbejdspartnere, der skal til for at skabe et produkt eller en serviceydelse med værdi for kunderne",
                        "<strong>Partners:</strong> Involves the partners needed to create a product or service of value to customers",
                    ),
                    (
                        "<strong>Økonomi:</strong> Ved, hvor indtægterne kommer fra, og hvordan omkostningerne opstår",
                        "<strong>Economics:</strong> Knows where revenue comes from and how costs arise",
                    ),
                ]
            ),
            p(
                "I de næste afsnit gennemgår vi de forskellige overordnede forretningsmodeller:",
                "In the next sections we go through the main types of business model:",
            ),
            li_items(
                [
                    (
                        "traditionelle forretningsmodeller fra den fysiske verden, og",
                        "traditional business models from the physical world, and",
                    ),
                    (
                        "digitale forretningsmodeller fra den digitale verden.",
                        "digital business models from the digital world.",
                    ),
                ]
            ),
            box(
                "facts",
                "Tre facts",
                "Three facts",
                li_items(
                    [
                        (
                            "En forretningsmodel forklarer, hvordan en virksomhed tjener penge",
                            "A business model explains how a company makes money",
                        ),
                        (
                            "Forretningsmodellen viser, hvilken værdi virksomheden skaber",
                            "The business model shows what value the company creates",
                        ),
                        (
                            "En forretningsmodel består af værditilbud, kunder, samarbejdspartnere og økonomi",
                            "A business model consists of value proposition, customers, partners and economics",
                        ),
                    ]
                ),
            ),
            box(
                "exercise",
                "Par-aktivitet",
                "Pair activity",
                "\n".join(
                    [
                        img(
                            IMG + "_processed_/c/e/csm_226_logoer_mobilpay_netflix_wolt_13d8b2f3e6.jpg"
                        ),
                        p(
                            "Du skal samarbejde med din sidemakker.",
                            "Work together with the person next to you.",
                        ),
                        li_items(
                            [
                                (
                                    "Vælg to virksomheder fra listen: Lego, Wolt, Espresso House, Netflix, MobilePay",
                                    "Choose two companies from the list: Lego, Wolt, Espresso House, Netflix, MobilePay",
                                ),
                                (
                                    "Undersøg for hver virksomhed og udfyld skemaet: Hvad tilbyder virksomheden? Hvem er kunderne? Hvordan tjener virksomheden penge? (fx salg, abonnement, reklamer, gebyrer)",
                                    "For each company, fill in a table: What does it offer? Who are the customers? How does it make money? (e.g. sales, subscription, ads, fees)",
                                ),
                                (
                                    "Diskutér: Hvad er de største ligheder og forskelle? Hvilken model virker mest attraktiv – og hvorfor?",
                                    "Discuss: What are the biggest similarities and differences? Which model seems most attractive – and why?",
                                ),
                            ],
                            ordered=True,
                        ),
                    ]
                ),
            ),
            box(
                "exercise",
                "Gruppe-aktivitet",
                "Group activity",
                "\n".join(
                    [
                        p("Du skal samarbejde med din gruppe.", "Work together with your group."),
                        p("Vælg én case:", "Choose one case:"),
                        li_items(
                            [
                                ("IKEA", "IKEA"),
                                ("Too Good To Go", "Too Good To Go"),
                                ("Airtox B2B", "Airtox B2B"),
                            ]
                        ),
                        li_items(
                            [
                                (
                                    "Hvad tilbyder virksomheden? (produkt eller ydelse)",
                                    "What does the company offer? (product or service)",
                                ),
                                ("Hvem er kunderne?", "Who are the customers?"),
                                (
                                    "Hvordan når virksomheden ud til kunderne? (fx app, butik, online, platform)",
                                    "How does the company reach customers? (e.g. app, store, online, platform)",
                                ),
                                (
                                    "Hvordan tjener virksomheden penge? (fx salg, abonnement, gebyrer)",
                                    "How does the company make money? (e.g. sales, subscription, fees)",
                                ),
                            ],
                            ordered=True,
                        ),
                    ]
                ),
            ),
        ]
    )


def s12() -> str:
    return "\n".join(
        [
            h2(
                "s12",
                "1.2 Traditionelle forretningsmodeller",
                "1.2 Traditional business models",
            ),
            p(
                "De traditionelle forretningsmodeller fandtes, før den digitale udvikling tog fart. De bruges dog stadig i dag.",
                "Traditional business models existed before the digital development took off. They are still used today.",
            ),
            p(
                "Inddelingen afhænger af, hvad virksomheden mest laver:",
                "The grouping depends on what the company mainly does:",
            ),
            nested_ul(
                [
                    (
                        "<strong>Produktionsvirksomheder</strong> – fremstiller varer.",
                        "<strong>Manufacturing companies</strong> – make goods.",
                    ),
                    (
                        "<strong>Handelsvirksomheder</strong> – køber og videresælger varer.",
                        "<strong>Trading companies</strong> – buy and resell goods.",
                        [
                            (
                                "Engrosvirksomheder sælger til detailhandlen.",
                                "Wholesalers sell to retailers.",
                            ),
                            (
                                "Detailvirksomheder sælger til forbrugerne.",
                                "Retailers sell to consumers.",
                            ),
                        ],
                    ),
                    (
                        "<strong>Servicevirksomheder</strong> – leverer ydelser.",
                        "<strong>Service companies</strong> – deliver services.",
                    ),
                ]
            ),
            h3(
                "Model: De traditionelle forretningsmodeller",
                "Model: Traditional business models",
            ),
            p(
                "Nedenfor vises en visuel oversigt over de tre hovedtyper af traditionelle forretningsmodeller:",
                "Below is a visual overview of the three main types of traditional business model:",
            ),
            li_items(
                [
                    (
                        "Produktionsvirksomheder, der fremstiller varer",
                        "Manufacturing companies that make goods",
                    ),
                    (
                        f"Handelsvirksomheder, der køber og videresælger varer – enten til andre virksomheder (<span class='term'>grossist</span>) eller direkte til forbrugerne (detail).",
                        f"Trading companies that buy and resell goods – either to other companies (<span class='term'>wholesaler</span>) or directly to consumers (retail).",
                    ),
                    (
                        "Servicevirksomheder, der sælger ydelser, fx timer.",
                        "Service companies that sell services, for example hours of work.",
                    ),
                ]
            ),
            p(
                "Når du har valgt forretningsmodel, bliver det lettere at forklare virksomhedens kunder og markeder.",
                "Once you have chosen a business model, it becomes easier to explain the company’s customers and markets.",
            ),
            img(
                IMG + "_processed_/5/c/csm_090_Traditionelle_forretningsmodeller_c09c050d05.png",
                "De traditionelle forretningsmodeller",
                "Traditional business models",
            ),
            box(
                "facts",
                "Tre facts",
                "Three facts",
                li_items(
                    [
                        (
                            "Traditionelle forretningsmodeller fandtes før den digitale udvikling og bruges stadig i dag",
                            "Traditional business models existed before digital development and are still used today",
                        ),
                        (
                            "Der er tre hovedtyper: produktions-, handels- og servicevirksomheder",
                            "There are three main types: manufacturing, trading and service companies",
                        ),
                        (
                            "Valg af forretningsmodel har betydning for kunder og markeder",
                            "The choice of business model matters for customers and markets",
                        ),
                    ]
                ),
            ),
            box(
                "exercise",
                "Par-aktivitet",
                "Pair activity",
                "\n".join(
                    [
                        p(
                            "Du skal løse opgaven sammen med din sidemakker.",
                            "Solve the task together with the person next to you.",
                        ),
                        p(
                            "1. Marker i skemaet den forretningsmodel, gruppen mener, virksomheden anvender som den primære. I skal vælge mellem:",
                            "1. In the table, mark the business model the group thinks the company uses as its primary model. Choose between:",
                        ),
                        li_items(
                            [
                                (
                                    "Produktionsvirksomhed: Fremstiller varer",
                                    "Manufacturing company: Makes goods",
                                ),
                                (
                                    "Handelsvirksomhed – Engros: Køber og sælger til detailhandlen",
                                    "Trading company – wholesale: Buys and sells to retailers",
                                ),
                                (
                                    "Handelsvirksomhed – Detail: Sælger direkte til forbrugerne",
                                    "Trading company – retail: Sells directly to consumers",
                                ),
                                (
                                    "Servicevirksomhed: Leverer ydelser",
                                    "Service company: Delivers services",
                                ),
                            ]
                        ),
                    ]
                ),
            ),
        ]
    )


def s13() -> str:
    return "\n".join(
        [
            h2("s13", "1.3 Digitale forretningsmodeller", "1.3 Digital business models"),
            p(
                "Digitale forretningsmodeller viser forskellige måder, virksomheder kan skabe værdi ved hjælp af digitale løsninger.",
                "Digital business models show different ways companies can create value using digital solutions.",
            ),
            p(
                "Det kan ske gennem salg af produkter, udvikling af digitale ydelser eller ved at stille digitale platforme til rådighed.",
                "This can happen through selling products, developing digital services, or by making digital platforms available.",
            ),
            p(
                "<strong>Figur 1.4</strong> giver et overblik over centrale typer af digitale forretningsmodeller.",
                "<strong>Figure 1.4</strong> gives an overview of key types of digital business model.",
            ),
            img(
                IMG + "_processed_/5/f/csm_091_Digitale_forretningsmodeller_6b12b2a535.png",
                "Digitale forretningsmodeller",
                "Digital business models",
            ),
            '<div class="model-grid">',
            _model_card(
                IMG + "_processed_/a/7/csm_099_Den_digitale_koebmand_125px_69857a9a68.png",
                "Den digitale købmand",
                "The digital merchant",
            ),
            _model_card(
                IMG + "_processed_/e/a/csm_100_Webshoppen_112px_5bd9216b8d.png",
                "Webshoppen",
                "The webshop",
            ),
            _model_card(
                IMG + "_processed_/a/8/csm_101_Den_digitale_producent_125px_2b56c64bde.png",
                "Den digitale producent",
                "The digital manufacturer",
            ),
            _model_card(
                IMG + "_processed_/5/6/csm_102_Softwareproducenten_125px_1e20fc84d2.png",
                "Softwareproducenten",
                "The software producer",
            ),
            _model_card(
                IMG + "_processed_/8/4/csm_103_Den_digitale_platformsbygger_125px_3047761b65.png",
                "Den digitale platformsbygger",
                "The digital platform builder",
            ),
            _model_card(
                IMG + "_processed_/b/8/csm_104_App-opfinderen_125px_227e1ed61c.png",
                "App-opfinderen",
                "The app inventor",
            ),
            _model_card(
                IMG + "_processed_/8/a/csm_105_Wiki-skaberen_125px_a57477d131.png",
                "Wiki-skaberen",
                "The wiki creator",
            ),
            "</div>",
            h3("Den digitale købmand", "The digital merchant"),
            p(
                "Den digitale købmand er en <strong>fysisk butik</strong>, der har udvidet sit salg ved at bruge internettet. Udgangspunktet er den traditionelle butik, som suppleres med en <strong>online butik</strong>.",
                "The digital merchant is a <strong>physical store</strong> that has expanded its sales by using the internet. The starting point is the traditional store, supplemented by an <strong>online store</strong>.",
            ),
            p(
                "Den digitale købmand kaldes også <strong>Brick-and-Click</strong>. Begrebet betyder, at kunden kan handle både i den fysiske butik (<em>Brick</em>) og online (<em>Click</em>) hos samme virksomhed.",
                "The digital merchant is also called <strong>Brick-and-Click</strong>. The term means that the customer can shop both in the physical store (<em>Brick</em>) and online (<em>Click</em>) with the same company.",
            ),
            p("Eksempler på en digital købmand er:", "Examples of a digital merchant are:"),
            li_items(
                [
                    ("Bilka.dk", "Bilka.dk"),
                    ("Elgiganten.dk", "Elgiganten.dk"),
                    ("Thansen.dk", "Thansen.dk"),
                ]
            ),
            h3("Webshoppen", "The webshop"),
            p(
                "Webshoppen er en butik, der som udgangspunkt <strong>kun findes på internettet</strong>.",
                "The webshop is a store that, as a starting point, <strong>only exists on the internet</strong>.",
            ),
            p(
                "Webshoppen køber varer fra produktionsvirksomheder og grossister og sælger dem videre online.",
                "The webshop buys goods from manufacturers and wholesalers and resells them online.",
            ),
            p(
                "Nogle webshops udvider senere med en fysisk butik. Denne model kaldes Click-and-Brick, hvor webshoppen er udgangspunktet, og den fysiske butik fungerer som supplement.",
                "Some webshops later expand with a physical store. This model is called Click-and-Brick, where the webshop is the starting point and the physical store is a supplement.",
            ),
            p("Eksempler på webshops er:", "Examples of webshops are:"),
            li_items(
                [
                    ("Boozt.com", "Boozt.com"),
                    ("KitchenOne.dk", "KitchenOne.dk"),
                    ("Løbeshop.dk", "Løbeshop.dk"),
                ]
            ),
            h3("Den digitale producent", "The digital manufacturer"),
            p(
                "Den digitale producent er en virksomhed, der tager udgangspunkt i produktion af fysiske produkter, men udvider forretningsmodellen med digitale tjenester, som er knyttet til produkterne.",
                "The digital manufacturer starts from the production of physical products, but expands the business model with digital services linked to those products.",
            ),
            p("Eksempler på digitale producenter er:", "Examples of digital manufacturers are:"),
            li_items(
                [
                    (
                        "Danfoss – temperaturen kan styres via en smartphone",
                        "Danfoss – the temperature can be controlled via a smartphone",
                    ),
                    (
                        "Philips – styrke og farve på el-pærer kan styres digitalt",
                        "Philips – brightness and colour of light bulbs can be controlled digitally",
                    ),
                    (
                        "Samsung – tv’et kobles på internettet",
                        "Samsung – the TV is connected to the internet",
                    ),
                ]
            ),
            p(
                "Produkterne fra de digitale producenter indgår ofte i kategorien: Internet of Things (IoT).",
                "Products from digital manufacturers often belong in the category Internet of Things (IoT).",
            ),
            h3("Softwareproducenten", "The software producer"),
            p(
                "Softwareproducenten udvikler software, som sælges som licenser.",
                "The software producer develops software that is sold as licences.",
            ),
            p(
                "Salget kan ske til både virksomheder og private.",
                "Sales can be to both companies and private customers.",
            ),
            p(
                "En særlig fordel ved software er, at det kan sælges igen og igen uden store ekstra omkostninger for producenten.",
                "A particular advantage of software is that it can be sold again and again without large extra costs for the producer.",
            ),
            p("Eksempel på softwareproducenter er:", "An example of a software producer is:"),
            li_items(
                [
                    (
                        "Microsoft, bl.a. ved salg af Office 365-licenser",
                        "Microsoft, for example through sales of Office 365 licences",
                    )
                ]
            ),
            h3("Den digitale platformsbygger", "The digital platform builder"),
            p(
                "Den digitale platformsbygger stiller en platform til rådighed.",
                "The digital platform builder makes a platform available.",
            ),
            p(
                "Platformen kan benyttes frit af én gruppe besøgende, mens det koster penge for en anden gruppe.",
                "The platform can be used for free by one group of visitors, while it costs money for another group.",
            ),
            p(
                "Eksempler på den digitale platformsbygger er:",
                "Examples of the digital platform builder are:",
            ),
            li_items(
                [
                    (
                        "Google – frit tilgængelig for alle, men koster penge for dem, der vil anvende platformen som annonceringsmedie",
                        "Google – freely available to everyone, but costs money for those who want to use the platform as an advertising medium",
                    ),
                    (
                        "Facebook – alle kan frit oprette og anvende en profil, men målrettet annoncering koster penge",
                        "Facebook – anyone can freely create and use a profile, but targeted advertising costs money",
                    ),
                    (
                        "DBA – hvis du sælger som privatperson i et begrænset omfang, er det gratis. Ønsker en virksomhed at sælge sine varer gennem DBA, koster det penge",
                        "DBA – if you sell as a private person on a limited scale, it is free. If a company wants to sell its goods through DBA, it costs money",
                    ),
                ]
            ),
            h3("App-opfinderen", "The app inventor"),
            p(
                "App-opfinderen er en virksomhed, der udvikler og driver apps.",
                "The app inventor is a company that develops and runs apps.",
            ),
            p(
                "Virksomheden tjener penge ved at forbinde brugere, der ønsker at købe og sælge, og tager typisk en lille procentdel af salget.",
                "The company makes money by connecting users who want to buy and sell, and typically takes a small percentage of the sale.",
            ),
            p(
                "Apps kan fx være spil eller handle om aktiviteter som træning eller dating. Nogle apps er gratis, mens andre kræver betaling eller <strong>abonnement</strong>.",
                "Apps can be games, for example, or cover activities such as training or dating. Some apps are free, while others require payment or a <strong>subscription</strong>.",
            ),
            p("Eksempler på app-opfindere er:", "Examples of app inventors are:"),
            li_items(
                [
                    ("Too Good To Go", "Too Good To Go"),
                    ("Airbnb", "Airbnb"),
                    ("The Sims", "The Sims"),
                    ("Endomondo", "Endomondo"),
                    ("Dating.dk", "Dating.dk"),
                ]
            ),
            img(
                IMG + "_processed_/6/7/csm_TGTG_logo_green_RGB_90118dd031.png",
                "Too Good To Go – logo",
                "Too Good To Go – logo",
            ),
            p(
                "Too Good To Go’s app forbinder virksomheder med overskudsvarer med forbrugere, der har behov for dem. En butik, der har varer, som er ved at overskride holdbarheden, kan sælge dem på appen til private forbrugere til en lavere pris.",
                "Too Good To Go’s app connects companies with surplus goods to consumers who need them. A shop with goods that are close to their expiry date can sell them on the app to private consumers at a lower price.",
            ),
            h3("Wiki-skaberen", "The wiki creator"),
            p(
                "Wiki-skaberen stiller en digital platform til rådighed, hvor brugerne selv skaber indholdet.",
                "The wiki creator makes a digital platform available where the users themselves create the content.",
            ),
            p("Eksempler på wiki-skaberen er:", "Examples of the wiki creator are:"),
            li_items([("Wikipedia", "Wikipedia"), ("Blogger.com", "Blogger.com")]),
            box(
                "facts",
                "Tre facts",
                "Three facts",
                li_items(
                    [
                        (
                            "Digitale forretningsmodeller skaber værdi ved hjælp af digitale løsninger",
                            "Digital business models create value using digital solutions",
                        ),
                        (
                            "Virksomheder kan tjene penge på produkter, digitale ydelser eller platforme",
                            "Companies can make money from products, digital services or platforms",
                        ),
                        (
                            "Der findes flere typer, fx webshop, digital producent og platform",
                            "There are several types, for example webshop, digital manufacturer and platform",
                        ),
                    ]
                ),
            ),
            box(
                "exercise",
                "Par-aktivitet",
                "Pair activity",
                "\n".join(
                    [
                        p(
                            "Du skal løse opgaven sammen med din sidemakker.",
                            "Solve the task together with the person next to you.",
                        ),
                        p(
                            "Vælg én af disse virksomheder: IKEA, Too Good To Go eller Airtox.",
                            "Choose one of these companies: IKEA, Too Good To Go or Airtox.",
                        ),
                        li_items(
                            [
                                (
                                    "Find to fordele ved virksomhedens digitale forretningsmodel.",
                                    "Find two advantages of the company’s digital business model.",
                                ),
                                (
                                    "Find to ulemper/udfordringer.",
                                    "Find two disadvantages/challenges.",
                                ),
                            ],
                            ordered=True,
                        ),
                    ]
                ),
            ),
        ]
    )


def _model_card(src: str, da: str, en: str) -> str:
    return (
        f'<div class="model-card"><img src="{src}" alt="" loading="lazy">'
        f"<p>{t(da, en)}</p></div>"
    )


def s14() -> str:
    return "\n".join(
        [
            h2(
                "s14",
                "1.4 Kombination af forretningsmodeller",
                "1.4 Combining business models",
            ),
            p(
                "Virksomheder udvikler og kombinerer forretningsmodeller for at:",
                "Companies develop and combine business models in order to:",
            ),
            li_items(
                [
                    ("øge salget", "increase sales"),
                    ("sænke omkostninger", "lower costs"),
                    ("tiltrække nye kunder", "attract new customers"),
                    ("yde bedre service", "provide better service"),
                ]
            ),
            p(
                f"Formålet er at imødekomme kundernes behov og skabe større omsætning. Det er jo ikke sikkert, at en simpel <span class='term'>forretningsmodel</span> kan bruges alene, men skal koble yderligere forhold på for at kunne fungere optimalt.",
                f"The purpose is to meet customers’ needs and create more revenue. A simple <span class='term'>business model</span> may not work on its own; extra elements often have to be added for it to work well.",
            ),
            h3(
                "Eksempler: Kombination af forretningsmodeller",
                "Examples: Combining business models",
            ),
            li_items(
                [
                    (
                        f"<strong>Frisør:</strong> <span class='term'>serviceydelse</span> kombineret med salg af hårprodukter",
                        f"<strong>Hairdresser:</strong> a <span class='term'>service</span> combined with sales of hair products",
                    ),
                    (
                        "<strong>Fitnesscenter:</strong> træning og hold kombineret med salg af fx proteinprodukter",
                        "<strong>Fitness centre:</strong> training and classes combined with sales of e.g. protein products",
                    ),
                ]
            ),
            p(
                "Forretningsmodeller er i konstant udvikling.",
                "Business models are constantly developing.",
            ),
            p(
                "Virksomheder ændrer og kombinerer dem for at finde nye måder at tjene penge på og tilpasse sig kundernes måde at handle på.",
                "Companies change and combine them to find new ways of making money and to adapt to how customers shop.",
            ),
            p(
                "Digitale muligheder har øget antallet af forretningsmodeller markant. I dette kapitel ser du nogle udvalgte kombinationer, men der findes mange flere.",
                "Digital opportunities have greatly increased the number of business models. In this chapter you see some selected combinations, but there are many more.",
            ),
            h3(
                "Kombination af fysisk butik og webshop",
                "Combining a physical store and a webshop",
            ),
            p(
                "Kombinationen af fysisk butik og webshop kan ske på flere måder.",
                "The combination of a physical store and a webshop can happen in several ways.",
            ),
            h4("Webshop til fysisk butik", "From webshop to physical store"),
            p(
                "Disse virksomheder starter digitalt med en webshop og åbner senere fysiske butikker.",
                "These companies start digitally with a webshop and later open physical stores.",
            ),
            p(
                'Man kalder dem for "Click-and-Brick", da de startede med at kunderne skulle klikke sig frem til at købe hos dem i deres webshop. Efterfølgende tilføjede de det fysiske køb til deres forretningsmodel.',
                'They are called "Click-and-Brick" because they started with customers clicking their way to a purchase in the webshop. Later they added physical purchase to their business model.',
            ),
            p("Eksempler på virksomheder:", "Examples of companies:"),
            li_items(
                [
                    ("Shaping New Tomorrow", "Shaping New Tomorrow"),
                    ("ditur.dk", "ditur.dk"),
                    ("Amazon", "Amazon"),
                ]
            ),
            h4("Fysisk butik til webshop", "From physical store to webshop"),
            p(
                "Disse virksomheder startede med kun at have fysiske butikker. Senere supplerer de med en webshop.",
                "These companies started with physical stores only. Later they add a webshop.",
            ),
            p(
                'Man kalder dem for "Brick-and-Click", da de gik fra kun at tilbyde det fysiske køb til også at tilbyde køb ved klik på produkter i deres webshop.',
                'They are called "Brick-and-Click" because they went from offering only physical purchase to also offering purchase by clicking products in their webshop.',
            ),
            p("Eksempler på virksomheder:", "Examples of companies:"),
            li_items(
                [
                    ("Elgiganten", "Elgiganten"),
                    ("Magasin du Nord", "Magasin du Nord"),
                    ("Bilka", "Bilka"),
                ]
            ),
            h3("Eksempel: Bestseller", "Example: Bestseller"),
            quote(
                "Bestseller kombinerer flere forretningsmodeller for at nå flere kunder.",
                "Bestseller combines several business models in order to reach more customers.",
            ),
            p(
                "Virksomheden sælger sine produkter gennem andre forhandlere og i egne butikker og webshops.",
                "The company sells its products through other retailers and in its own stores and webshops.",
            ),
            p(
                "I webshops kan kunderne se hele sortimentet. De fysiske butikker har derfor kun udvalgte varer på lager.",
                "In the webshops, customers can see the full range. The physical stores therefore only stock selected items.",
            ),
            p(
                "Kombinationen giver bedre service for kunderne:",
                "The combination gives customers better service:",
            ),
            li_items(
                [
                    (
                        "Kunder, der ønsker vejledning og inspiration, kan gå i butik.",
                        "Customers who want advice and inspiration can go to the store.",
                    ),
                    (
                        "Kunder, der vil handle hurtigt og selvstændigt, kan bruge webshoppen.",
                        "Customers who want to shop quickly and independently can use the webshop.",
                    ),
                ]
            ),
            p(
                "Figur 1.5 viser, hvordan Bestseller bruger flere salgskanaler på samme tid for at øge salget og tilpasse sig forskellige kunders behov.",
                "Figure 1.5 shows how Bestseller uses several sales channels at the same time to increase sales and adapt to different customers’ needs.",
            ),
            img(
                IMG + "_processed_/2/d/csm_006_Bestsellers_forretningsmodel_27df25b5d3.png",
                "Bestsellers forretningsmodel",
                "Bestseller’s business model",
            ),
            h3("Abonnementsordninger", "Subscription models"),
            p(
                "En forretningsmodel, der anvendes både online og offline, er abonnementsmodellen. I rigtig mange år har man kunnet købe abonnement på aviser, blade og magasiner. Abonnementer sikrer, at kunden får leveret en ydelse eller et produkt med jævne mellemrum uden at foretage sig noget.",
                "A business model used both online and offline is the subscription model. For many years it has been possible to subscribe to newspapers, magazines and journals. Subscriptions ensure that the customer receives a service or product at regular intervals without having to do anything.",
            ),
            p(
                "Der findes grundlæggende tre modeller for abonnementer:",
                "There are basically three subscription models:",
            ),
            li_items(
                [
                    ("Genopfyldnings-abonnement", "Replenishment subscription"),
                    ("Præference-abonnement", "Curation / preference subscription"),
                    ("Adgangs-abonnement", "Access subscription"),
                ]
            ),
            p(
                "Der er ofte fire elementer, man skal forholde sig til, når man arbejder med abonnementsordninger:",
                "There are often four elements to consider when working with subscriptions:",
            ),
            li_items(
                [
                    ("Prøveperiode", "Trial period"),
                    ("Medlemspakker", "Membership packages"),
                    ("Betalingsperioder", "Payment periods"),
                    ("Binding", "Commitment / lock-in"),
                ]
            ),
            h4("Prøveperiode", "Trial period"),
            p(
                "Hvis en virksomhed ønsker at sælge mange abonnementer så hurtigt som muligt, er en gratis prøveperiode eller en lav intropris en god idé. Den nye abonnent kan prøve produktet eller servicen og finde ud af, om det lever op til forventningerne. Hvis abonnenten bliver skuffet, kan abonnenten melde sig ud igen, uden at det har kostet noget.",
                "If a company wants to sell many subscriptions as quickly as possible, a free trial or a low intro price is a good idea. The new subscriber can try the product or service and see if it meets expectations. If the subscriber is disappointed, they can cancel without it having cost anything.",
            ),
            p(
                "Virksomheden skal dog være opmærksom på tre ting, når den skaffer nye abonnenter gennem en gratis prøveperiode.",
                "The company should, however, be aware of three things when it acquires new subscribers through a free trial.",
            ),
            li_items(
                [
                    (
                        "Virksomheden vil formentlig tabe penge på abonnenten i prøveperioden.",
                        "The company will probably lose money on the subscriber during the trial period.",
                    ),
                    (
                        "Nogle abonnenter vil være gratister, der måske forsvinder igen, når prøveperioden er ovre. Abonnenter, der tilmelder sig uden tilbuddet om en gratis prøveperiode, vil være mere loyale.",
                        "Some subscribers will be free-riders who may disappear when the trial ends. Subscribers who sign up without a free trial will be more loyal.",
                    ),
                    (
                        "Der vil være stor risiko for, at personer, der allerede er abonnenter, vil føle sig snydt. Nye abonnenter betaler intet eller meget lidt, mens trofaste abonnenter betaler fuld pris.",
                        "There is a high risk that existing subscribers will feel cheated. New subscribers pay nothing or very little, while loyal subscribers pay full price.",
                    ),
                ]
            ),
            h4("Medlemspakker", "Membership packages"),
            p(
                "Ved mange services skal abonnenten vælge mellem et udvalg af forskellige medlemspakker. Hvis man bestiller et tv-abonnement gennem Telia, kan man vælge mellem tre forskellige medlemspakker, der aktuelt kaldes 4ONE, 4MORE og 4ALL. Prisen på abonnementet vil afhænge af, hvilken medlemspakke man vælger. Det giver abonnenten en vis fleksibilitet, at man forholdsvis enkelt kan skifte fra den ene medlemspakke til den anden.",
                "For many services the subscriber must choose between different membership packages. If you order a TV subscription through Telia, you can choose between three packages currently called 4ONE, 4MORE and 4ALL. The price depends on which package you choose. It gives the subscriber some flexibility that it is fairly easy to switch from one package to another.",
            ),
            h4("Betalingsperioder", "Payment periods"),
            p(
                "De fleste digitale services, som fx abonnementer på telefon og streaming, har en betalingsperiode på en måned. Det betyder, at abonnenten betaler et lille beløb hver måned i stedet for et stort beløb hvert halve eller hele år. Nogle abonnementsordninger giver rabat, hvis abonnenter betaler et år ud i fremtiden. Det sikrer nemlig, at forholdet til abonnenten fastholdes i en længere periode.",
                "Most digital services, such as phone and streaming subscriptions, have a one-month payment period. That means the subscriber pays a small amount each month instead of a large amount every six or twelve months. Some subscriptions give a discount if subscribers pay a year ahead. That helps keep the relationship with the subscriber for a longer period.",
            ),
            h4("Binding", "Commitment / lock-in"),
            p(
                "Der er ikke ret mange forbrugere, der ønsker at være bundet til et abonnement i en længere periode. De fleste ønsker mulighed for at komme ud af et abonnementsforhold så hurtigt som muligt. Stort set alle abonnementsordninger er derfor helt uden binding – eller maksimalt med binding i den periode, abonnenten allerede har betalt for.",
                "Not many consumers want to be locked into a subscription for a long period. Most want to be able to leave as quickly as possible. Almost all subscriptions are therefore fully without lock-in – or at most locked in for the period the subscriber has already paid for.",
            ),
            box(
                "facts",
                "Tre facts",
                "Three facts",
                li_items(
                    [
                        (
                            "Virksomheder kombinerer ofte flere forretningsmodeller",
                            "Companies often combine several business models",
                        ),
                        (
                            "Formålet er fx at øge salg, tiltrække kunder og give bedre service",
                            "The purpose is, for example, to increase sales, attract customers and give better service",
                        ),
                        (
                            "En typisk kombination er fysisk butik og webshop",
                            "A typical combination is a physical store and a webshop",
                        ),
                    ]
                ),
            ),
            box(
                "exercise",
                "Gruppe-aktivitet",
                "Group activity",
                "\n".join(
                    [
                        p(
                            "I skal i grupper vælge én af virksomhederne:",
                            "In groups, choose one of the companies:",
                        ),
                        li_items(
                            [
                                ("IKEA", "IKEA"),
                                ("Too Good To Go", "Too Good To Go"),
                                ("Airtox B2B", "Airtox B2B"),
                            ]
                        ),
                        li_items(
                            [
                                (
                                    "Beskriv virksomhedens forretningsmodel.",
                                    "Describe the company’s business model.",
                                ),
                                (
                                    "Er den et eksempel på Click-and-Brick, Brick-and-Click eller en tredje variant?",
                                    "Is it an example of Click-and-Brick, Brick-and-Click, or a third variant?",
                                ),
                                (
                                    "Hvorfor kombinerer virksomheden flere kanaler?",
                                    "Why does the company combine several channels?",
                                ),
                                (
                                    "Diskutér: Hvordan kunne virksomheden tilføje endnu en salgskanal?",
                                    "Discuss: How could the company add yet another sales channel?",
                                ),
                            ],
                            ordered=True,
                        ),
                    ]
                ),
            ),
        ]
    )


def s15() -> str:
    return "\n".join(
        [
            h2(
                "s15",
                "1.5 Bæredygtige forretningsmodeller",
                "1.5 Sustainable business models",
            ),
            p("Bæredygtige forretningsmodeller handler om at:", "Sustainable business models are about:"),
            li_items(
                [
                    ("bruge færre ressourcer", "using fewer resources"),
                    ("genbruge materialer", "reusing materials"),
                    ("undgå spild", "avoiding waste"),
                ]
            ),
            p(
                "Fokus er ikke på at producere og sælge mest muligt, men på at lave produkter, der:",
                "The focus is not on producing and selling as much as possible, but on making products that:",
            ),
            li_items(
                [
                    ("holder længere", "last longer"),
                    ("kan repareres", "can be repaired"),
                    ("kan genbruges eller skilles ad", "can be reused or taken apart"),
                ]
            ),
            h3("Cirkulær økonomi", "Circular economy"),
            p(
                "Bæredygtige forretningsmodeller bygger på cirkulær økonomi.",
                "Sustainable business models are based on the circular economy.",
            ),
            p("Det betyder, at virksomheder:", "That means companies:"),
            li_items(
                [
                    (
                        "reducerer ressourceforbrug, fx el og vand",
                        "reduce resource use, for example electricity and water",
                    ),
                    ("mindsker affald", "reduce waste"),
                    (
                        "designer produkter til genbrug og reparation",
                        "design products for reuse and repair",
                    ),
                ]
            ),
            p(
                "Det er et brud med den lineære tankegang, hvor produkter hurtigt ender som affald.",
                "This breaks with linear thinking, where products quickly end up as waste.",
            ),
            h3("Hvad handler bæredygtighed om?", "What is sustainability about?"),
            p("Bæredygtighed handler især om:", "Sustainability is especially about:"),
            li_items(
                [
                    ("at undgå overforbrug", "avoiding overconsumption"),
                    ("at reducere CO₂-udledning", "reducing CO₂ emissions"),
                ]
            ),
            p(
                "En gennemsnitsdansker bruger i dag ressourcer svarende til over 4 jordkloder om året. Målet er at komme ned på 2–3 tons CO₂ pr. person årligt.",
                "An average Dane today uses resources equivalent to more than 4 Earths per year. The goal is to get down to 2–3 tonnes of CO₂ per person per year.",
            ),
            p("Overforbrug er den største udfordring.", "Overconsumption is the biggest challenge."),
            h3(
                "Den grønne pagt (Det indre grønne marked 2030)",
                "The Green Deal (The internal green market 2030)",
            ),
            p(
                "EU arbejder for en mere cirkulær økonomi, hvor virksomheder skal tage større ansvar.",
                "The EU is working for a more circular economy, where companies must take greater responsibility.",
            ),
            p("Den grønne pagt indeholder bl.a.:", "The Green Deal includes, among other things:"),
            li_items(
                [
                    ("etablering af cirkulær økonomi", "establishing a circular economy"),
                    ("øget producentansvar (take back)", "increased producer responsibility (take-back)"),
                    ("krav om reparation", "requirements for repair"),
                    ("bekæmpelse af greenwashing", "fighting greenwashing"),
                ]
            ),
            p(
                "Det er svært for én virksomhed at blive cirkulær alene. Derfor er partnerskaber ofte nødvendige.",
                "It is difficult for one company to become circular on its own. That is why partnerships are often necessary.",
            ),
            h3(
                "Sommerfuglemodellen – teknisk materialestrøm",
                "The butterfly diagram – technical material flow",
            ),
            p(
                "Sommerfuglemodellen viser, hvordan ressourcer kan cirkulere.",
                "The butterfly diagram shows how resources can circulate.",
            ),
            p("Modellen består af to kredsløb:", "The model consists of two cycles:"),
            li_items(
                [
                    ("Biologisk kredsløb (ikke behandlet her)", "Biological cycle (not covered here)"),
                    ("Teknisk kredsløb (fokus i dette kapitel)", "Technical cycle (the focus of this chapter)"),
                ]
            ),
            p(
                "Den tekniske del viser, hvordan produkter kan holdes i brug gennem:",
                "The technical side shows how products can be kept in use through:",
            ),
            li_items(
                [
                    ("reparation", "repair"),
                    ("genbrug", "reuse"),
                    ("opgradering", "upgrade"),
                    ("genfremstilling", "remanufacturing"),
                ]
            ),
            p(
                "Målet er at holde materialer i omløb så længe som muligt og minimere affald.",
                "The goal is to keep materials in circulation for as long as possible and minimise waste.",
            ),
            img(
                "https://afs-fc-eudeux.systime.dk/fileadmin/indhold/Rentegninger/087_sommerfugle-modellen_419px.svg",
                "Sommerfuglemodellen",
                "The butterfly diagram",
            ),
            p(
                "Figur 1.6 illustrerer højresiden af sommerfuglemodellen, som fokuserer på de tekniske materialer, der anvendes i produktionen af varer.",
                "Figure 1.6 illustrates the right-hand side of the butterfly diagram, which focuses on the technical materials used in the production of goods.",
            ),
            h3("Forskellige grader af bæredygtighed", "Different degrees of sustainability"),
            table(
                [
                    ("Grad", "Degree"),
                    ("Loop", "Loop"),
                    ("Forklaring og eksempler", "Explanation and examples"),
                ],
                [
                    [
                        ("1", "1"),
                        ("Deling/Salg", "Sharing/Sale"),
                        (
                            "Dette loop er det mest bæredygtige. Det handler om at dele produkter med andre eller sælge overskudsvarer videre. Eksempler: GoMore, Too Good To Go, Røde Kors’ genbrugsbutikker.",
                            "This loop is the most sustainable. It is about sharing products with others or reselling surplus goods. Examples: GoMore, Too Good To Go, Red Cross second-hand shops.",
                        ),
                    ],
                    [
                        ("2", "2"),
                        ("Reparation og vedligeholdelse", "Repair and maintenance"),
                        (
                            "Her forlænger virksomheder produktets levetid ved at tilbyde reparation og vedligeholdelse. Eksempler: Lokale hælebarer og skræddere.",
                            "Here companies extend the product’s lifetime by offering repair and maintenance. Examples: Local cobblers and tailors.",
                        ),
                    ],
                    [
                        ("3", "3"),
                        ("Istandsættelse", "Refurbishment"),
                        (
                            "Istandsætte og opdatere defekte, slidte eller forældede produkter. Eksempler: Refurb og Autoparts24.",
                            "Refurbish and update defective, worn or outdated products. Examples: Refurb and Autoparts24.",
                        ),
                    ],
                    [
                        ("4", "4"),
                        ("Genfremstilling", "Remanufacturing"),
                        (
                            "Anvende materialer fra brugte produkter eller restprodukter til at lave nye varer. Eksempler: Cotopaxi og Pleasant.",
                            "Use materials from used products or leftover materials to make new goods. Examples: Cotopaxi and Pleasant.",
                        ),
                    ],
                    [
                        ("5", "5"),
                        ("Genanvendelse af råstoffer", "Recycling of raw materials"),
                        (
                            "Adskille defekte produkter, sortere materialer og genanvende råstofferne i nye produkter. Eksempel: Stena Recycling.",
                            "Take defective products apart, sort materials and recycle the raw materials into new products. Example: Stena Recycling.",
                        ),
                    ],
                ],
            ),
            h3("Det merkantile dilemma", "The commercial dilemma"),
            p("Virksomheder står i et dilemma:", "Companies face a dilemma:"),
            li_items(
                [
                    ("de skal tjene penge", "they must make money"),
                    ("men samtidig reducere ressourceforbrug", "but at the same time reduce resource use"),
                ]
            ),
            h3("Eksempel: Elgiganten", "Example: Elgiganten"),
            p(
                f"Elgiganten tjener normalt penge på at sælge nye produkter. I en mere bæredygtig <span class='term'>forretningsmodel</span> kan de i stedet også tjene penge på at forlænge produkternes levetid.",
                f"Elgiganten normally makes money by selling new products. In a more sustainable <span class='term'>business model</span> they can also make money by extending the lifetime of products.",
            ),
            p("Det kan fx være:", "That can for example be:"),
            li_items(
                [
                    ("reparation af elektronik", "repair of electronics"),
                    ("serviceaftaler", "service agreements"),
                    ("salg af reservedele", "sales of spare parts"),
                ]
            ),
            p(
                "På den måde sælges der ikke kun nye produkter – der skabes også indtjening på eksisterende produkter.",
                "In this way it is not only new products that are sold – income is also created from existing products.",
            ),
            p(
                "Den største udfordring er, om virksomheder kan omlægge deres forretning, så de både er mere bæredygtige og stadig tjener penge.",
                "The biggest challenge is whether companies can change their business so that they are both more sustainable and still make money.",
            ),
            h3("Transformation af mindset", "A change of mindset"),
            p("Virksomheder skal skifte fokus:", "Companies need to shift their focus:"),
            li_items(
                [
                    ("fra mere produktion", "from more production"),
                    ("til bedre produktion", "to better production"),
                ]
            ),
            p("<strong>Lineær økonomi</strong>", "<strong>Linear economy</strong>"),
            li_items(
                [
                    ("fokus på vækst og salg", "focus on growth and sales"),
                    ("bæredygtighed som et CSR-ansvar", "sustainability as a CSR responsibility"),
                ]
            ),
            p("<strong>Cirkulær økonomi</strong>", "<strong>Circular economy</strong>"),
            li_items(
                [
                    ("fokus på ansvar og fællesskab", "focus on responsibility and community"),
                    ("bæredygtighed er alles ansvar", "sustainability is everyone’s responsibility"),
                ]
            ),
            table(
                [
                    ("Mindset i den lineære økonomi", "Mindset in the linear economy"),
                    ("Mindset i den cirkulære økonomi", "Mindset in the circular economy"),
                ],
                [
                    [
                        ("Naturen er en ressource, der tilhører os", "Nature is a resource that belongs to us"),
                        (
                            "Naturen er et fællesskab, som vi er en del af",
                            "Nature is a community that we are part of",
                        ),
                    ],
                    [
                        (
                            "Bæredygtighed er noget, de arbejder med i CSR-afdelingen",
                            "Sustainability is something they work with in the CSR department",
                        ),
                        (
                            "Alle i organisationen kan bidrage til bæredygtighed",
                            "Everyone in the organisation can contribute to sustainability",
                        ),
                    ],
                    [
                        ("Vi skal vinde over de andre", "We must beat the others"),
                        ("Vi vinder sammen", "We win together"),
                    ],
                    [
                        ("Mere produktion", "More production"),
                        ("Bedre produktion", "Better production"),
                    ],
                ],
            ),
            h3("Eksempel: IKEA og bæredygtighed", "Example: IKEA and sustainability"),
            img(
                IMG + "_processed_/3/6/csm_IKEA_2018_sRGB_25_red_1a9896cfd2.png",
                "IKEA – logo",
                "IKEA – logo",
            ),
            p("IKEA arbejder aktivt med bæredygtighed ved at:", "IKEA works actively with sustainability by:"),
            li_items(
                [
                    ("designe møbler, der kan skilles ad", "designing furniture that can be taken apart"),
                    ("bruge genanvendelige materialer", "using recyclable materials"),
                    ("tilbyde reservedele", "offering spare parts"),
                    ("vejlede kunder i vedligeholdelse", "guiding customers on maintenance"),
                ]
            ),
            p(
                "Målet er at blive en 100 % cirkulær virksomhed.",
                "The goal is to become a 100% circular company.",
            ),
            p("Prøv at gå ind på ikea.com", "Try going to ikea.com"),
            li_items(
                [
                    (
                        "Tips og idéer til en mere ressourcebevidst livsstil",
                        "Tips and ideas for a more resource-conscious lifestyle",
                    ),
                    ("En bedre hverdag", "A better everyday life"),
                ]
            ),
            box(
                "facts",
                "Tre facts",
                "Three facts",
                li_items(
                    [
                        (
                            "Bæredygtige forretningsmodeller handler om at bruge færre ressourcer og undgå spild",
                            "Sustainable business models are about using fewer resources and avoiding waste",
                        ),
                        (
                            "Virksomheder arbejder med cirkulær økonomi, hvor produkter genbruges, repareres og holder længere",
                            "Companies work with a circular economy, where products are reused, repaired and last longer",
                        ),
                        (
                            "Fokus er på bedre produktion i stedet for mere produktion",
                            "The focus is on better production instead of more production",
                        ),
                    ]
                ),
            ),
            box(
                "exercise",
                "Par-aktivitet",
                "Pair activity",
                "\n".join(
                    [
                        p(
                            "Du og din makker skal finde eksempler på, hvordan produkter i en cirkulær økonomi kan forblive i brug – i stedet for at ende som affald.",
                            "You and your partner should find examples of how products in a circular economy can stay in use – instead of ending up as waste.",
                        ),
                        li_items(
                            [
                                (
                                    "Læs udtrækket om cirkulær økonomi og de fem loops.",
                                    "Read the extract about the circular economy and the five loops.",
                                ),
                                (
                                    "Vælg ét produkt, I begge kender (fx smartphone, tøj, sko, cykel).",
                                    "Choose one product you both know (e.g. smartphone, clothes, shoes, bicycle).",
                                ),
                                (
                                    "Hvordan kan produktet indgå i hvert af de fem loops?",
                                    "How can the product take part in each of the five loops?",
                                ),
                                (
                                    "Hvilket loop er mest realistisk – og hvorfor?",
                                    "Which loop is most realistic – and why?",
                                ),
                            ],
                            ordered=True,
                        ),
                    ]
                ),
            ),
            box(
                "exercise",
                "Gruppe-aktivitet",
                "Group activity",
                "\n".join(
                    [
                        p(
                            "Du skal samarbejde med din gruppe. Vælg én case:",
                            "Work with your group. Choose one case:",
                        ),
                        li_items(
                            [
                                ("IKEA", "IKEA"),
                                ("Too Good To Go", "Too Good To Go"),
                                ("Airtox", "Airtox"),
                            ]
                        ),
                        p(
                            "Arbejd med spørgsmålene, og præsenter jeres svar for en anden gruppe.",
                            "Work with the questions, and present your answers to another group.",
                        ),
                        li_items(
                            [
                                ("Vælg en virksomhed.", "Choose a company."),
                                (
                                    "Læs om cirkulær økonomi og det tekniske kredsløb.",
                                    "Read about the circular economy and the technical cycle.",
                                ),
                                (
                                    "Hvor er virksomheden i dag ift. cirkulær økonomi?",
                                    "Where is the company today in relation to the circular economy?",
                                ),
                                (
                                    "Hvilke tiltag kunne styrke cirkulariteten frem mod 2030?",
                                    "Which actions could strengthen circularity towards 2030?",
                                ),
                                (
                                    "Hvordan kan forretningsmodellen stadig skabe et tilfredsstillende overskud, hvis fokus er at mindske salg af nye varer?",
                                    "How can the business model still create a satisfactory profit if the focus is to reduce sales of new goods?",
                                ),
                            ],
                            ordered=True,
                        ),
                        p(
                            'Forbered en <strong>kort pitch</strong>: "Sådan bliver din virksomhed både bæredygtig og overskudsgivende."',
                            'Prepare a <strong>short pitch</strong>: "This is how your company becomes both sustainable and profitable."',
                        ),
                        p("Fremlæg for en anden gruppe.", "Present to another group."),
                    ]
                ),
            ),
        ]
    )


def s16() -> str:
    return "\n".join(
        [
            h2("s16", "1.6 AI i forretningsmodeller", "1.6 AI in business models"),
            p(
                "Kunstig intelligens er en del af hverdagen for mange virksomheder, og udviklingen går hurtigt. Det handler ikke kun om teknologi, men om at ændre den måde, virksomheder arbejder på.",
                "Artificial intelligence is part of everyday life for many companies, and development is moving fast. It is not only about technology, but about changing the way companies work.",
            ),
            p(
                "AI giver nye muligheder for effektivitet og innovation, fx:",
                "AI gives new opportunities for efficiency and innovation, for example:",
            ),
            li_items(
                [
                    (
                        "<strong>Mere tid:</strong> Rutineopgaver kan automatiseres, så medarbejderne kan fokusere på de vigtige beslutninger.",
                        "<strong>More time:</strong> Routine tasks can be automated, so employees can focus on the important decisions.",
                    ),
                    (
                        "<strong>Bedre idéer:</strong> AI kan analysere store mængder data og komme med forslag, som mennesker måske ikke selv finder.",
                        "<strong>Better ideas:</strong> AI can analyse large amounts of data and suggest ideas that people might not find themselves.",
                    ),
                    (
                        "<strong>Større kundeværdi:</strong> Virksomheder kan tilpasse produkter og service præcist til kundernes behov.",
                        "<strong>Greater customer value:</strong> Companies can adapt products and service precisely to customers’ needs.",
                    ),
                ]
            ),
            p(
                "Til sidst handler det om at styrke konkurrenceevnen – og samtidig gøre kunderne mere tilfredse.",
                "In the end it is about strengthening competitiveness – and at the same time making customers more satisfied.",
            ),
            h3("Virksomheders brug af AI", "Companies’ use of AI"),
            p(
                "Tre ud af fire danske virksomheder bruger allerede AI eller forventer at gøre det inden for kort tid.",
                "Three out of four Danish companies already use AI or expect to do so shortly.",
            ),
            p(
                'Kilde: <a href="https://www.danskindustri.dk/future-of-work/nyhedsarkiv/2025/6/7-ud-af-10-virksomheder-bruger-nu-generativ-ai/" target="_blank" rel="noopener">7 ud af 10 virksomheder bruger nu generativ AI – Dansk Industri</a>',
                'Source: <a href="https://www.danskindustri.dk/future-of-work/nyhedsarkiv/2025/6/7-ud-af-10-virksomheder-bruger-nu-generativ-ai/" target="_blank" rel="noopener">7 out of 10 companies now use generative AI – Confederation of Danish Industry</a>',
            ),
            h3("Junckers (gulvproducent)", "Junckers (flooring manufacturer)"),
            img(IMG + "_processed_/3/c/csm_Junckers_4479052157.jpg"),
            p(
                "Junckers laver og sælger trægulve til både private hjem og virksomheder.",
                "Junckers makes and sells wooden floors for both private homes and companies.",
            ),
            p(
                "Når de skal markedsføre deres produkter, bruger de AI til at skrive reklamer, blogindlæg og produktbeskrivelser.",
                "When they market their products, they use AI to write ads, blog posts and product descriptions.",
            ),
            p(
                "Det betyder, at AI hjælper med at finde gode ord og vendinger, så teksterne bliver spændende og professionelle. I stedet for at en medarbejder skal starte helt fra bunden, får de et færdigt forslag fra AI, som de bagefter kan rette til.",
                "That means AI helps find good words and phrases, so the texts become engaging and professional. Instead of an employee starting from scratch, they get a draft from AI which they can then edit.",
            ),
            p(
                "<strong>Fordel:</strong> Sparer tid og får flere idéer til kreative tekster.",
                "<strong>Advantage:</strong> Saves time and generates more ideas for creative texts.",
            ),
            h3("Coolshop (webshop)", "Coolshop (webshop)"),
            img(IMG + "_processed_/3/a/csm_Coolshop_c2fb7aeebc.png"),
            p(
                "Coolshop er en stor dansk webshop, hvor man kan købe alt fra spil og elektronik til legetøj.",
                "Coolshop is a large Danish webshop where you can buy everything from games and electronics to toys.",
            ),
            p(
                "De bruger AI til kundeservice – for eksempel at svare på spørgsmål om levering eller produkter.",
                "They use AI for customer service – for example answering questions about delivery or products.",
            ),
            p(
                "AI hjælper også med at oversætte produkttekster, så kunder i Norge, Sverige og Finland kan læse teksten på deres eget sprog. I stedet for at betale for mange oversættelser, laver AI en hurtig version, som medarbejderne bagefter tjekker igennem.",
                "AI also helps translate product texts so customers in Norway, Sweden and Finland can read the text in their own language. Instead of paying for many translations, AI makes a quick version which employees then check.",
            ),
            p(
                "<strong>Fordel:</strong> Hurtigere service til kunder og bedre oplevelse i flere lande.",
                "<strong>Advantage:</strong> Faster service for customers and a better experience in several countries.",
            ),
            h3("Dinero (regnskab)", "Dinero (accounting)"),
            img(IMG + "_processed_/1/3/csm_Dinero_2ec82c596c.jpeg"),
            p(
                "Dinero er et online regnskabsprogram, som hjælper små virksomheder med at holde styr på penge og bilag.",
                "Dinero is an online accounting program that helps small companies keep track of money and receipts.",
            ),
            p(
                "De bruger AI til at registrere timer og opdatere bogholderiet automatisk. For eksempel kan AI selv genkende en kvittering og placere den det rigtige sted i regnskabet, uden at en medarbejder skal gøre det manuelt.",
                "They use AI to register hours and update the accounts automatically. For example, AI can recognise a receipt and place it in the right place in the accounts, without an employee doing it by hand.",
            ),
            p(
                "AI kan også minde virksomhederne om vigtige ting, som fx momsfrister.",
                "AI can also remind companies of important things, such as VAT deadlines.",
            ),
            p(
                "<strong>Fordel:</strong> Mindre manuelt arbejde og færre fejl i regnskabet.",
                "<strong>Advantage:</strong> Less manual work and fewer errors in the accounts.",
            ),
            h3("Samarbejdet mellem menneske og maskine", "Cooperation between human and machine"),
            p(
                "AI er et stærkt værktøj, men det kan ikke stå alene.",
                "AI is a powerful tool, but it cannot stand alone.",
            ),
            p(
                "Selvom AI kan skrive tekster, svare kunder eller lave beregninger, er der ting, som kun mennesker kan gøre godt nok. Derfor skal mennesker stadig hjælpe – og det arbejdes der med i næsten alle virksomheder.",
                "Even though AI can write texts, answer customers or do calculations, there are things that only humans can do well enough. That is why humans still need to help – and almost all companies work with this.",
            ),
            p("Mennesker er vigtige for at:", "Humans are important in order to:"),
            li_items(
                [
                    (
                        "<strong>Kontrollere fakta:</strong> AI kan tage fejl eller bruge gamle oplysninger. Mennesker skal dobbelttjekke, om det er rigtigt.",
                        "<strong>Check facts:</strong> AI can be wrong or use old information. Humans must double-check whether it is correct.",
                    ),
                    (
                        "<strong>Tilpasse sproget til kunderne:</strong> AI skriver ofte korrekt, men sproget kan virke for generelt. Kun mennesker forstår helt kundernes tone og kultur.",
                        "<strong>Adapt the language to customers:</strong> AI often writes correctly, but the language can feel too generic. Only humans fully understand customers’ tone and culture.",
                    ),
                    (
                        f"<strong>Bruge kreativ og kritisk tænkning:</strong> AI kan finde mønstre og komme med forslag, men det forstår ikke <span class='term'>værdier</span>, målgrupper eller virksomhedsstrategi.",
                        f"<strong>Use creative and critical thinking:</strong> AI can find patterns and make suggestions, but it does not understand <span class='term'>values</span>, target groups or company strategy.",
                    ),
                ]
            ),
            p(
                "Dette kaldes <strong>Human in the Loop</strong>. Det betyder, at mennesker og AI arbejder sammen og tjekker hinanden. Når de gør det, bliver resultatet bedst.",
                "This is called <strong>Human in the Loop</strong>. It means that humans and AI work together and check each other. When they do that, the result is best.",
            ),
            h3("Fordele og udfordringer ved AI", "Advantages and challenges of AI"),
            table(
                [("Fordele", "Advantages"), ("Udfordringer", "Challenges")],
                [
                    [
                        (
                            "Hurtigere arbejde: Mange opgaver klares på meget kortere tid. Lavere omkostninger: Virksomheder sparer penge, fordi mindre tid bruges på rutinearbejde. Bedre kundeoplevelser: AI kan lave personlige anbefalinger og give hurtige svar.",
                            "Faster work: Many tasks are done in much less time. Lower costs: Companies save money because less time is spent on routine work. Better customer experiences: AI can make personal recommendations and give quick answers.",
                        ),
                        (
                            "AI kan lave fejl: Hvis ingen tjekker, kan der komme forkerte oplysninger ud til kunder eller i regnskaber. Overfladiske løsninger: AI kan misse detaljer, der kræver erfaring eller menneskelig forståelse. Nye kompetencer er nødvendige: Medarbejdere skal lære at bruge AI og vurdere dens kvalitet.",
                            "AI can make mistakes: If nobody checks, incorrect information can reach customers or accounts. Superficial solutions: AI can miss details that require experience or human understanding. New skills are needed: Employees must learn to use AI and assess its quality.",
                        ),
                    ]
                ],
            ),
            box(
                "facts",
                "Tre facts",
                "Three facts",
                li_items(
                    [
                        (
                            f"Når virksomheder bruger AI i deres <span class='term'>forretningsmodel</span>, kan de automatisere opgaver og spare både tid og penge",
                            f"When companies use AI in their <span class='term'>business model</span>, they can automate tasks and save both time and money",
                        ),
                        (
                            "AI giver mulighed for at udvikle nye produkter og services, der skaber værdi for kunderne",
                            "AI makes it possible to develop new products and services that create value for customers",
                        ),
                        (
                            "Den bedste løsning er ofte AI + mennesker sammen, hvor mennesker sikrer kvalitet og kreative beslutninger (Human in the Loop)",
                            "The best solution is often AI + humans together, where humans ensure quality and creative decisions (Human in the Loop)",
                        ),
                    ]
                ),
            ),
            box(
                "exercise",
                "Gruppe-aktivitet",
                "Group activity",
                "\n".join(
                    [
                        p(
                            "I skal i grupper på 3-4 personer vælge én af virksomhederne:",
                            "In groups of 3–4 people, choose one of the companies:",
                        ),
                        li_items(
                            [
                                ("IKEA", "IKEA"),
                                ("Too Good To Go", "Too Good To Go"),
                                ("Airtox B2B", "Airtox B2B"),
                            ]
                        ),
                        p("<strong>Opgave</strong>", "<strong>Task</strong>"),
                        p("Diskutér:", "Discuss:"),
                        li_items(
                            [
                                (
                                    "Hvor i forretningsmodellen kunne AI gøre størst forskel? (fx produktudvikling, kundeservice, logistik, prissætning, markedsføring)",
                                    "Where in the business model could AI make the biggest difference? (e.g. product development, customer service, logistics, pricing, marketing)",
                                ),
                                (
                                    "Kom med ét konkret forslag til, hvordan virksomheden kan bruge AI. (Beskriv kort hvordan og hvilken gevinst det giver).",
                                    "Give one concrete suggestion for how the company can use AI. (Briefly describe how, and what gain it gives).",
                                ),
                                (
                                    "Hvorfor skal mennesker stadig være en del af løsningen?",
                                    "Why should humans still be part of the solution?",
                                ),
                            ],
                            ordered=True,
                        ),
                        p("<strong>Præsentation</strong>", "<strong>Presentation</strong>"),
                        p("Hver gruppe laver et 1-minutters pitch:", "Each group makes a 1-minute pitch:"),
                        li_items(
                            [
                                ("Jeres virksomhed", "Your company"),
                                ("Jeres AI-forslag", "Your AI suggestion"),
                                (
                                    "Hvorfor det styrker forretningsmodellen",
                                    "Why it strengthens the business model",
                                ),
                            ]
                        ),
                    ]
                ),
            ),
        ]
    )


def s17() -> str:
    return "\n".join(
        [
            h2("s17", "1.7 Opgaver til kapitel 1", "1.7 Exercises for chapter 1"),
            h3("Opgavetyper", "Types of exercises"),
            p("På opgavesiden finder du:", "On the exercise page you will find:"),
            li_items(
                [
                    ("Opgaver om begreber og metoder", "Exercises on concepts and methods"),
                    ("Caseopgaver", "Case assignments"),
                    ("Gruppeopgave", "Group assignment"),
                    ("Opgave med AI", "Assignment with AI"),
                ]
            ),
            h3("Opgave 1.1: Produktionsvirksomheder", "Exercise 1.1: Manufacturing companies"),
            p(
                "Identificér 10 forskellige produktionsvirksomheder.",
                "Identify 10 different manufacturing companies.",
            ),
            p(
                "Forklar, hvorfor du mener, at de identificerede virksomheder følger forretningsmodellen for produktionsvirksomheder.",
                "Explain why you think the companies you identified follow the manufacturing business model.",
            ),
            h3("Opgave 1.2: Grossister", "Exercise 1.2: Wholesalers"),
            p(
                f'Foretag en googlesøgning på ordet "<span class="term">grossist</span>", og find fem forskellige grossister.',
                f'Do a Google search for the word "<span class="term">wholesaler</span>", and find five different wholesalers.',
            ),
            p(
                "Undersøg, hvilken branche hver af de fem grossister befinder sig inden for.",
                "Investigate which industry each of the five wholesalers operates in.",
            ),
            h3("Opgave 1.3: Lokale detailhandlere", "Exercise 1.3: Local retailers"),
            p(
                "Identificér 10 forskellige detailhandlere inden for dit lokalområde.",
                "Identify 10 different retailers in your local area.",
            ),
            p(
                "Redegør for, hvad du som kunde forventer dig af de forskellige detailhandlere, når du træder ind i butikken.",
                "Explain what you as a customer expect from the different retailers when you walk into the store.",
            ),
            h3("Opgave 1.4: Lokale servicevirksomheder", "Exercise 1.4: Local service companies"),
            p(
                "Identificér 10 forskellige servicevirksomheder i dit lokalområde.",
                "Identify 10 different service companies in your local area.",
            ),
            p(
                "Beskriv den eller de tjenester, de hver især tilbyder kunderne.",
                "Describe the service or services each of them offers customers.",
            ),
            h3(
                "Opgave 1.5: Forretningsmodellen for Joe &amp; The Juice",
                "Exercise 1.5: The business model of Joe &amp; The Juice",
            ),
            img(IMG + "_processed_/1/2/csm_joe_and_the_juice_logo_red_788681f379.png"),
            p(
                "Forestil dig, at du er en tur på cafe/restauranten Joe &amp; The Juice, hvor du får dig en sandwich og en smoothie.",
                "Imagine you visit the café/restaurant Joe &amp; The Juice, where you have a sandwich and a smoothie.",
            ),
            li_items(
                [
                    (
                        "Redegør for det fysiske produkt ved besøget på Joe &amp; The Juice.",
                        "Explain the physical product of the visit to Joe &amp; The Juice.",
                    ),
                    (
                        "Redegør for serviceydelsen ved besøget på Joe &amp; The Juice.",
                        "Explain the service of the visit to Joe &amp; The Juice.",
                    ),
                    (
                        f"Diskutér, om Joe &amp; The Juices <span class='term'>forretningsmodel</span> er <span class='term'>produktionsvirksomhed</span>, <span class='term'>handelsvirksomhed</span> eller <span class='term'>servicevirksomhed</span>.",
                        f"Discuss whether Joe &amp; The Juice’s <span class='term'>business model</span> is a <span class='term'>manufacturing company</span>, a <span class='term'>trading company</span> or a <span class='term'>service company</span>.",
                    ),
                ],
                ordered=True,
            ),
            h3(
                "Opgave 1.6: Forretningsmodellen for Too Good To Go",
                "Exercise 1.6: The business model of Too Good To Go",
            ),
            p(
                f"Diskutér, hvor forretningsmodellen for Too Good To Go skal ligge på skalaen i figuren: Fra fysisk produkt til <span class='term'>serviceydelse</span>.",
                f"Discuss where Too Good To Go’s business model should sit on the scale in the figure: From physical product to <span class='term'>service</span>.",
            ),
            img(
                IMG + "_processed_/9/2/csm_005_Fra_fysisk_produkt_a396b487ba.png",
                "Fra fysisk produkt til serviceydelse",
                "From physical product to service",
            ),
            h3("Opgave 1.7: Digitale forretningsmodeller", "Exercise 1.7: Digital business models"),
            p(
                "Med udgangspunkt i de digitale forretningsmodeller skal du identificere tre konkrete virksomheder inden for hver af de syv digitale forretningsmodeller.",
                "Based on the digital business models, identify three concrete companies within each of the seven digital business models.",
            ),
            h3("Opgave 1.8: Abonnementsordninger", "Exercise 1.8: Subscription models"),
            li_items(
                [
                    (
                        "Redegør for begrebet abonnementsordning.",
                        "Explain the concept of a subscription model.",
                    ),
                    (
                        "Redegør for de tre forskellige abonnementsmodeller.",
                        "Explain the three different subscription models.",
                    ),
                    (
                        "Find et eksempel på hver af de tre abonnementsmodeller.",
                        "Find an example of each of the three subscription models.",
                    ),
                    (
                        "Diskuter med din sidemand, hvilke fordele en virksomhed har ved at anvende abonnementsordning som forretningsmodel.",
                        "Discuss with the person next to you what advantages a company has from using a subscription as its business model.",
                    ),
                ],
                ordered=True,
            ),
            h3("Opgave 1.9: Cirkulær økonomi", "Exercise 1.9: Circular economy"),
            li_items(
                [
                    ("Redegør for begrebet cirkulær økonomi.", "Explain the concept of circular economy."),
                    (
                        "Redegør for indholdet i Sommerfuglemodellen.",
                        "Explain the content of the butterfly diagram.",
                    ),
                    (
                        "Her finder du en liste over virksomheder og produkter. Undersøg de enkelte virksomheder og produkter, og brug sommerfuglemodellen til at forklare, hvordan de understøtter cirkulær økonomi.",
                        "Here is a list of companies and products. Investigate each one, and use the butterfly diagram to explain how they support the circular economy.",
                    ),
                ],
                ordered=True,
            ),
            li_items(
                [
                    ("GreenMind", "GreenMind"),
                    ("R.U.M. stol", "R.U.M. chair"),
                    ("Create2STAY", "Create2STAY"),
                    ("REPAIR CAFE DK", "REPAIR CAFE DK"),
                    ("RE-ZIP", "RE-ZIP"),
                    ("ReCollector", "ReCollector"),
                    ("Skomageri.dk", "Skomageri.dk"),
                ]
            ),
            h3(
                "Caseopgave 1.10: Zalando og REMA 1000 – Forretningsmodeller",
                "Case assignment 1.10: Zalando and REMA 1000 – Business models",
            ),
            img(IMG + "_processed_/2/5/csm_Zalando_bc03e398a7.png"),
            p(
                f"Zalando er en af de største spillere på det danske marked for e-handel. De har et <span class='term'>sortiment</span> på mere end 5.800 brands og sælger til kunder i 25 lande. Det er et tysk firma, men Anders Holch Povlsen fra Bestseller ejer en del af virksomheden.",
                f"Zalando is one of the biggest players on the Danish e-commerce market. They have an <span class='term'>assortment</span> of more than 5,800 brands and sell to customers in 25 countries. It is a German company, but Anders Holch Povlsen from Bestseller owns part of it.",
            ),
            img(IMG + "_processed_/a/f/csm_REMA_1000_Logo_da32b0d4b3.png"),
            p(
                "REMA 1000 er en af landets største dagligvarekæder med et meget stort antal fysiske butikker samt en webshop.",
                "REMA 1000 is one of the country’s largest grocery chains, with a very large number of physical stores as well as a webshop.",
            ),
            h4("Formål", "Purpose"),
            li_items(
                [
                    (
                        "Demonstrere viden om forretningsmodeller",
                        "Demonstrate knowledge of business models",
                    ),
                    (
                        "Redegøre for konkrete traditionelle og digitale forretningsmodeller",
                        "Explain concrete traditional and digital business models",
                    ),
                ]
            ),
            h4("Proces", "Process"),
            p(
                "Enkeltvis eller i små grupper – brug 1 time.",
                "Individually or in small groups – use 1 hour.",
            ),
            h4("Produkt", "Product"),
            p(
                "Forbered 3-5 dias til en præsentation på klassen af ca. 5-7 minutters varighed.",
                "Prepare 3–5 slides for a class presentation of about 5–7 minutes.",
            ),
            h4("Kilder", "Sources"),
            p("Søg flere oplysninger via:", "Search for more information via:"),
            li_items([("Zalando", "Zalando"), ("REMA 1000", "REMA 1000")]),
            h4("Spørgsmål", "Questions"),
            p(
                "Du skal i besvarelsen af nedenstående spørgsmål inddrage både Zalando og REMA 1000.",
                "In your answers to the questions below, include both Zalando and REMA 1000.",
            ),
            li_items(
                [
                    ("Forklar, hvad en forretningsmodel er.", "Explain what a business model is."),
                    (
                        "Bestem, hvilken traditionel forretningsmodel REMA 1000 bygger på, og anvend figur 1.2 til at beskrive REMA 1000’s forretningsmodel.",
                        "Determine which traditional business model REMA 1000 is based on, and use figure 1.2 to describe REMA 1000’s business model.",
                    ),
                    (
                        "Bestem, hvilke digitale forretningsmodeller Zalando bygger på, og anvend figur 1.4 til at beskrive Zalando’s forretningsmodel.",
                        "Determine which digital business models Zalando is based on, and use figure 1.4 to describe Zalando’s business model.",
                    ),
                    (
                        "Redegør, med udgangspunkt i Zalando, for de fordele og ulemper virksomheden kunne have ved at tilbyde kunderne en af de tre abonnementsordninger, der er nævnt i afsnit 1.4.",
                        "Using Zalando as a starting point, explain the advantages and disadvantages the company could have from offering customers one of the three subscription models mentioned in section 1.4.",
                    ),
                    (
                        "Vurder og begrund, hvilke forretningsmodeller du mener, der får størst succes i de kommende fem år.",
                        "Assess and justify which business models you think will be most successful in the next five years.",
                    ),
                ],
                ordered=True,
            ),
            h3(
                "Caseopgave 1.11: IKEA – Bæredygtige forretningsmodeller",
                "Case assignment 1.11: IKEA – Sustainable business models",
            ),
            img(
                IMG + "_processed_/3/6/csm_IKEA_2018_sRGB_25_red_d8245459d4.png",
                "IKEA – logo",
                "IKEA – logo",
            ),
            p(
                "IKEA er en global møbelvirksomhed, der arbejder aktivt med bæredygtighed og cirkulær økonomi.",
                "IKEA is a global furniture company that works actively with sustainability and the circular economy.",
            ),
            p(
                "Virksomheden har fokus på at forlænge produkters levetid, reducere affald og tilbyde løsninger, der gør det nemt for kunderne at reparere og genbruge møbler.",
                "The company focuses on extending product lifetime, reducing waste and offering solutions that make it easy for customers to repair and reuse furniture.",
            ),
            h4("Formål", "Purpose"),
            li_items(
                [
                    (
                        "Demonstrere viden om bæredygtige og cirkulære forretningsmodeller.",
                        "Demonstrate knowledge of sustainable and circular business models.",
                    ),
                    (
                        "Redegøre for konkrete tiltag i det tekniske kredsløb.",
                        "Explain concrete actions in the technical cycle.",
                    ),
                    (
                        "Vurdere, hvordan IKEA håndterer det merkantile dilemma.",
                        "Assess how IKEA handles the commercial dilemma.",
                    ),
                ]
            ),
            h4("Proces", "Process"),
            li_items(
                [
                    ("Enkeltvis eller i små grupper.", "Individually or in small groups."),
                    ("Brug ca. 1 time.", "Use about 1 hour."),
                ]
            ),
            h4("Kilder", "Sources"),
            p("Søg flere oplysninger via:", "Search for more information via:"),
            li_items(
                [
                    ("Kapitel 1.5", "Chapter 1.5"),
                    (
                        '<a href="https://www.ikea.com/dk/da/this-is-ikea/climate-environment/ikea-baeredygtighedsstrategi-pubfea4c210/" target="_blank" rel="noopener">IKEA’s hjemmeside om bæredygtighedsstrategi</a>',
                        '<a href="https://www.ikea.com/dk/da/this-is-ikea/climate-environment/ikea-baeredygtighedsstrategi-pubfea4c210/" target="_blank" rel="noopener">IKEA’s website on its sustainability strategy</a>',
                    ),
                ]
            ),
            h4("Spørgsmål", "Questions"),
            li_items(
                [
                    (
                        "Forklar, hvad cirkulær økonomi er, og hvordan IKEA arbejder med det tekniske kredsløb i Sommerfuglemodellen.",
                        "Explain what the circular economy is, and how IKEA works with the technical cycle in the butterfly diagram.",
                    ),
                    (
                        "Beskriv mindst tre konkrete tiltag, IKEA har taget for at forlænge levetiden af deres produkter.",
                        "Describe at least three concrete actions IKEA has taken to extend the lifetime of their products.",
                    ),
                    (
                        "Redegør for, hvordan IKEA håndterer det merkantile dilemma mellem at sælge mange produkter og samtidig være bæredygtig.",
                        "Explain how IKEA handles the commercial dilemma between selling many products and being sustainable at the same time.",
                    ),
                    (
                        "Vurder, hvilke loops i det tekniske kredsløb IKEA især arbejder med, og giv eksempler.",
                        "Assess which loops in the technical cycle IKEA especially works with, and give examples.",
                    ),
                    (
                        "Diskutér, hvordan et øget fokus på klima og miljø hos både kunder og medarbejdere kan understøtte IKEAs bæredygtige forretningsmodel.",
                        "Discuss how a greater focus on climate and environment among both customers and employees can support IKEA’s sustainable business model.",
                    ),
                ],
                ordered=True,
            ),
            h3(
                "Gruppeopgave 1.12: Skab udvikling i din lokale virksomhed",
                "Group assignment 1.12: Create development in your local company",
            ),
            h4(
                "Del 1: Valg af virksomhed og indledende analyse",
                "Part 1: Choosing a company and initial analysis",
            ),
            li_items(
                [
                    (
                        "Din gruppe skal vælge en lokal virksomhed, I ønsker at arbejde med.",
                        "Your group must choose a local company you want to work with.",
                    ),
                    (
                        "Lav en kort beskrivelse af, hvorfor den pågældende virksomhed er valgt.",
                        "Write a short description of why that company was chosen.",
                    ),
                    (
                        "Hvilken branche befinder virksomheden sig i?",
                        "Which industry is the company in?",
                    ),
                    (
                        "Redegør for, om det er en traditionel, digital eller en kombineret forretningsmodel.",
                        "Explain whether it is a traditional, digital or combined business model.",
                    ),
                ],
                ordered=True,
            ),
            h4("Del 2: Udvikling af forretningsmodel", "Part 2: Developing the business model"),
            p(
                "I skal nu tænke kreativt og komme med bud på udvikling af virksomhedens nuværende forretningsmodel.",
                "You should now think creatively and come up with ideas for developing the company’s current business model.",
            ),
            li_items(
                [
                    (
                        "Lav en brainstorming, hvor der tænkes ud af boksen i forhold til, hvordan virksomheden kan udvikle deres forretningsmodel.",
                        "Brainstorm out of the box about how the company can develop its business model.",
                    ),
                    (
                        "Vælg den model, der giver bedst mening.",
                        "Choose the model that makes the most sense.",
                    ),
                    (
                        "Beskriv den nye model og redegør for, hvorfor forslaget vil gøre virksomheden stærkere i fremtiden.",
                        "Describe the new model and explain why the proposal will make the company stronger in the future.",
                    ),
                ],
                ordered=True,
            ),
            h4("Del 3: Forberedelse af fremlæggelse", "Part 3: Preparing the presentation"),
            p(
                "Gør klar til en fremlæggelse af forretningsmodellen for virksomhedens ledelse (her klassen).",
                "Prepare a presentation of the business model for the company’s management (here: the class).",
            ),
            li_items(
                [
                    ("Hvorfor er virksomheden valgt?", "Why was the company chosen?"),
                    (
                        "Hvilke emner var oppe at vende ved brainstormingen?",
                        "Which topics came up in the brainstorm?",
                    ),
                    (
                        "Hvad var baggrunden for at arbejde videre med den valgte forretningsmodel?",
                        "What was the reason for continuing with the chosen business model?",
                    ),
                    ("Beskriv den nye forretningsmodel.", "Describe the new business model."),
                    (
                        "Redegør for, hvorfor denne model vil gøre virksomheden stærkere i fremtiden.",
                        "Explain why this model will make the company stronger in the future.",
                    ),
                ],
                ordered=True,
            ),
            h3("Opgave 1.13: Human in the loop", "Exercise 1.13: Human in the loop"),
            p(
                "Du skal bruge et AI-værktøj, som er godkendt af din skole.",
                "You must use an AI tool that is approved by your school.",
            ),
            p("<strong>Opgave</strong>", "<strong>Task</strong>"),
            p("Du arbejder med én af disse virksomheder:", "You work with one of these companies:"),
            li_items(
                [
                    ("REMA 1000", "REMA 1000"),
                    ("Pandora", "Pandora"),
                    ("Vero Moda", "Vero Moda"),
                ]
            ),
            li_items(
                [
                    (
                        "Spørg AI om idéer: Bed AI om tre måder, virksomheden kan bruge AI til at styrke sin forretningsmodel. Skriv både spørgsmålet og AI’s svar ind i din opgave.",
                        "Ask AI for ideas: Ask AI for three ways the company can use AI to strengthen its business model. Write both the question and AI’s answer into your assignment.",
                    ),
                    (
                        "Vælg og begrund: Hvilken af AI’s idéer synes du er bedst – og hvorfor? Her skal du selv vurdere, hvordan idéen skaber værdi for kunden eller virksomheden.",
                        "Choose and justify: Which of AI’s ideas do you think is best – and why? Here you must assess how the idea creates value for the customer or the company.",
                    ),
                    (
                        "Tjek for fejl: Er der noget i AI’s forslag, der virker urealistisk eller problematisk? Skriv mindst ét eksempel.",
                        "Check for errors: Is there anything in AI’s suggestion that seems unrealistic or problematic? Write at least one example.",
                    ),
                ],
                ordered=True,
            ),
            p(
                "<strong>Refleksion: Human in the Loop</strong>",
                "<strong>Reflection: Human in the Loop</strong>",
            ),
            p("Skriv kort:", "Write briefly:"),
            li_items(
                [
                    (
                        "Hvad kunne AI ikke vide om virksomheden, som du kan bruge din viden til at vurdere?",
                        "What could AI not know about the company, which you can use your knowledge to assess?",
                    ),
                    (
                        "Hvad siger det om, hvorfor mennesker stadig er nødvendige?",
                        "What does that say about why humans are still necessary?",
                    ),
                ]
            ),
        ]
    )


def s18() -> str:
    return "\n".join(
        [
            h2("s18", "1.8 Begrebstræning i kapitel 1", "1.8 Term practice in chapter 1"),
            p("Her kan du træne kapitlets fagbegreber:", "Here you can practise the chapter’s terms:"),
            li_items(
                [
                    (
                        "Oversigt over kapitlets vigtigste fagbegreber",
                        "Overview of the chapter’s most important terms",
                    ),
                    ("5 skarpe til kapitlet", "5 sharp questions on the chapter"),
                    (
                        "En træningsopgave med begrebskort",
                        "A practice task with term cards",
                    ),
                ]
            ),
            h3("Vigtige begreber i kapitel 1", "Important terms in chapter 1"),
            nested_ul(
                [
                    ("Forretningsmodel", "Business model"),
                    (
                        "Traditionelle forretningsmodeller",
                        "Traditional business models",
                        [
                            ("Produktionsvirksomhed", "Manufacturing company"),
                            ("Handelsvirksomhed", "Trading company"),
                            ("Grossist", "Wholesaler"),
                            ("Detailhandel", "Retail"),
                            ("Servicevirksomhed", "Service company"),
                        ],
                    ),
                    (
                        "Digitale forretningsmodeller",
                        "Digital business models",
                        [
                            ("Den digitale købmand", "The digital merchant"),
                            ("Webshoppen", "The webshop"),
                            ("Den digitale producent", "The digital manufacturer"),
                            ("Softwareproducenten", "The software producer"),
                            ("Den digitale platformsbygger", "The digital platform builder"),
                            ("App-opfinderen", "The app inventor"),
                            ("Wiki-skaberen", "The wiki creator"),
                        ],
                    ),
                    (
                        "Kombination af forretningsmodeller",
                        "Combining business models",
                        [("Abonnementsordninger", "Subscription models")],
                    ),
                ]
            ),
            h3("5 skarpe til kapitel 1", "5 sharp questions on chapter 1"),
            li_items(
                [
                    (
                        "Hvad er definitionen på en forretningsmodel?",
                        "What is the definition of a business model?",
                    ),
                    (
                        "Hvilke elementer indgår som byggesten i en forretningsmodel?",
                        "Which elements are the building blocks of a business model?",
                    ),
                    (
                        "Hvilket begreb dækker over både detailhandler og grossister?",
                        "Which term covers both retailers and wholesalers?",
                    ),
                    ("Hvad er en digital producent?", "What is a digital manufacturer?"),
                    (
                        "Nævn fire digitale forretningsmodeller.",
                        "Name four digital business models.",
                    ),
                ],
                ordered=True,
            ),
            h3("Træn begreber i kapitel 1", "Practise terms in chapter 1"),
            p(
                "Du skal øve fagbegreberne i kapitel 1, så du kan huske dem og forklare deres betydning.",
                "You should practise the terms in chapter 1 so you can remember them and explain what they mean.",
            ),
            p(
                "Din lærer udleverer begrebskort og giver instruktion.",
                "Your teacher hands out term cards and gives instructions.",
            ),
            p(
                "Du skal samarbejde med dine klassekammerater om at skabe en fælles forståelse for kapitlets indhold.",
                "You should work with your classmates to build a shared understanding of the chapter content.",
            ),
        ]
    )
