from django.core.management import BaseCommand
from quote.models import Quote

class Command(BaseCommand):

    def handle(self, *args, **options):
        for line in import_data.splitlines():
            parts = line.split(", Obamacare")
            try:
                name = parts[0]
                body = parts[1]

                quote = Quote.objects.create(name=name, body=body)
            except IndexError:
                continue



import_data = """
Mike, Obamacare ate my babies!
Mike, Obamacare took my virginity.
Kevin, Obamacare sunk the Titanic!
Mike, Obamacare spoiled the ending of Breaking Bad!
Kevin, Obamacare caused 9/11!
Mike, Obamacare bombed Pearl Harbor!
Kevin, Obamacare killed Heath Ledger!
Mike, Obamacare cancelled Firefly!
Kevin, Obamacare started Nickelback!
Mike, Obamacare cast Ben Affleck.
Kevin, Obamacare dodged the draft.
Mike, Obamacare inhaled.
Kevin, Obamacare is responsible for world hunger!
Mike, Obamacare twerked in front of my daughter.
Kevin, Obamacare has WMDs!
Mike, Obamacare killed the radio star.
Kevin, Obamacare assassinated JFK!
Mike, Obamacare tapped out the keg.
Kevin, Obamacare firebombed my village!
Mike, Obamacare scratched all my DVDs.
Kevin, Obamacare dropped my call.
Mike, Obamacare made me late for work.
Kevin, Obamacare made me watch The Jersey Shore.
Mike, Obamacare ran over Stephen King.
Kevin, Obamacare broke up the Beatles!
Mike, Obamacare told me it loved me, then left me after I gave it up.
Mike, Obamacare left legos all over the floor and I stepped on them barefoot.
Mike, Obamacare poured sugar into my gas tank.
Wes, Obamacare makes cat litter that specifically doesn't hide the smell of cat
Mike, Obamacare cut down the rainforest.
Wes, Obamacare made the Indian on the litter commercial
Mike, Obamacare tied my shoelaces together.
Wes, Obamacare told John Locke what he cant
Mike, Obamacare was Keyser Soze.
Wes, Obamacare always gets the thimble when it plays
Mike, Obamacare sold me a fake gold chain in the parking lot.
Wes, Obamacare ate all the rye chips out of my Gardetto's snack
Mike, Obamacare switched the labels for anal cream with hand sanitizer.
Mike, Obamacare wants to eliminate all gingers.
Greg, Obamacare to help speed the soul harvest via granda and the death pannels.
Jordan, Obamacare made me gay.
Mike, Obamacare flashed its naughty bits in front of my grandma.
Wes, Obamacare smells of elderberries.
Jordan, Obamacare faked the moon landing.
Wes, Obamacare smells of elderberries.
Wes, Obamacare is one of the HUMAN cast members in Transformers
Jordan, Obamacare took Kristen Stewart's emotions.
Mike, Obamacare gave me 70's bush.
Greg, Obamacare caused the HIV outbreak in the porn industry.
Mike, Obamacare gave Mama Cass that ham sandwhich.
Jordan, Obamacare replaced all my capitalisms with socialisms.
Mike, Obamacare caused my hair to grey.
Jordan, Obamacare was actually born in Kenya.
Mike, Obamacare will keep my kid on my insurance all the way through college!
Mike, Obamacare did not shut down the government.
Mary, Obamacare is the real
Mike, Obamacare shot J.R.
Kevin, Obamacare murdered JonBenet Ramsey!
Mike, Obamacare killed all the dinosaurs.
Mike, Obamacare took away Mary's clean underwear.
Sean, Obamacare is Honey Boo Boo's Daddy!
Sean, Obamacare peed on the seat.
Mike, Obamacare doesn't want you to know that Biden cares too.
Kevin, Obamacare was D.B. Cooper.
Mike, Obamacare keyed my car.
Mike, Obamacare is the best there is at what it does and it ain't very nice. Bub.
Mike, Obamacare renewed The Kardashians for another season.
Greg, Obamacare scared Christopher Reeves horse.
Wes, Obamacare is reading this right NOW.
Mike, Obamacare ghost directed The Godfather Part III.
Wes, Obamacare spilled spaghetti on the sofa......again.....DAMMIT!!!
Mike, Obamacare didn't do it! It was the one armed man!
Greg, Obamacare took Walt.
Wes, Obamacare made me wear parachute pants in high school....just once though...
Mike, Obamacare is your father.
Kevin, Obamacare banned Pete Rose from the Hall of Fame!
Mike, Obamacare always said stupid is as stupid does.
Kevin, Obamacare or Yo-mommacare?
Kevin, Obamacare started the Chicago fire!
Kevin, Obamacare hates children!
Mike, Obamacare keeps changing my privacy settings.
Kevin, Obamacare watched me in the shower.
Kevin, Obamacare got an eyefull.
Mike, Obamacare overdosed me on Viagra. Now I'm a eunuch.
Kevin, Obamacare stole my lawn ornaments!
Mike, Obamacare tried to milk my moobs. They're kinda sore now.
Greg, Obamacare obamacared.
Mike, Obamacare used nair on my scrote.
Kevin, Obamacare vajazzled you!
Mike, Obamacare did it all for the nookie.
Greg, Obamacare and the hotdog flavored water.
Mike, Obamacare should've known better than to cheat a friend. Now it's never gonna dance again.
Jordan, Obamacare killed the younglings!
Jordan, Obamacare shot the Sheriff...but it did not shoot the deputy.
Mike, Obamacare was the walrus. Goo goo g'joob!
Mike, Obamacare will cut off your johnson Lebowski!
Greg, Obamacare are nihilists. THEY CARE ABOUT NOTHINK!
Mike, Obamacare clogged my toilet.
Greg, Obamacare down but it shall become more powerful than you ever imagined.
Mike, Obamacare took my donation but didn't give me my Kickstarter reward.
Mike, Obamacare laughed at me because I misread the internet and missed Saturday Night Live.
Mike, Obamacare doesn't cover zombie vaccinations.
Greg, Obamacare made me walk in a national
Greg, Obamacare shut down the government
Greg, Obamacare shoved me over and broke my
Greg, Obamacare wouldnt let nobody come rescue me.
Greg, Obamacare lead a bear to me and it ate my ass.
Greg, Obamacare made that bear
Mike, Obamacare is going to teach Greg some respect.
Greg, Obamacare made you deliver a dead guys meds.
Mike, Obamacare made me offer the widow "company"
Greg, Obamacare made her accept.
Mike, Obamacare made her like it.
Mike, Obamacare is a grand old party pooper.
Mike, Obamacare dropped the ball on the whole website thing.
Greg, Obamacare did. Its working xompletely as of yesterday, for , e anywqy.
Casey, Obamacare phished my twitter
Greg, Obamacare shared my nudies on 4chan.
Casey, Obamacare took the last three pumpkins from the pumpkin patch and made children cry.
Mike, Obamacare replaced my windshield wipers with Brillo pads.
Greg, Obamacare threw that candybar in the pool.
Mike, Obamacare chased my wife with mistletoe at her works office party.
Casey, Obamacare peed in my laundry basket.
Mike, Obamacare waited until you were home before telling you where it hid your car keys.
Casey, Obamacare uses speakerphone in crowded public spaces.
Mike, Obamacare holds the phone out in front of its face like it's going to eat it.
Casey, Obamacare uses #hashtags in non social media contexts.
Greg, Obamacare let that gorilla out the zoo that done punched Bobby Boucet in the eye.
Jordan, Obamacare got its chocolate in my peanut butter!
Casey, Obamacare double dipped in the cheese dip.
Jordan, Obamacare used my favorite shirt as a dishrag.
Jordan, Obamacare ate all the GOOD chocolates in the box and left me with just the coconut ones. Yuck!
Greg, Obamacare ate all the catpoop out of the litter box.
Jordan, Obamacare took Ched-kitty's missing leg!
Mike, Obamacare punched me in the dick and took my lunch money. Twice.
Jordan, Obamacare DID have sexual relations with that woman...Ms. Lewinski.
Mike, Obamacare took me to a Carrot Top show.
Greg, Obamacare laughed the loudest.
Casey, Obamacare posted my SSN on 4chan.
Greg, Obamacare brought down that wall.
Mike, Obamacare doesn't listen to anything I say. It just nods while looking down at its phone whenever I try to talk.
Greg Lemons Too busy trying to sign up for Obamacare.
Kevin, Obamacare just made me lose "The Game"!
Mike, Obamacare gave me a kidney stone.
Kevin, Obamacare take it away?
Kevin, Obamacare gonna ruin your peehole!
Mike, Obamacare makes when he asks me to cough.
Mike, Obamacare reminded me that Suzanne Somers is still alive.
Mike, Obamacare called Joseph a racist.
Greg, Obamacare made Joseph tell her to go sit in the back of the bus. She bravely refused.
Mike, Obamacare sits in its own damn seat, damnt!
Mike, Obamacare can time travel!
Mike, Obamacare sold heroin to Phillip Seymour Hoffman
Mike, Obamacare made it snow.
Greg, Obamacare slid your truck off the road.
Mike, Obamacare wouldn't pick me up in its four wheel drive.
Lenny, Obamacare took all the labels off my can goods.
Mike, Obamacare is to blame when I forget I have yearly deductibles!
Lenny, Obamacare wants to remake ALL the movies from the '80s. (i.e. Total Recall, Robocop) No more originals!
Mike, Obamacare raised the price on Marvel Legends.
Lenny, Obamacare is already on Mars waiting for us to catch up.
Lenny, Obamacare torched the Majestic.
Mike, Obamacare tripped Jennifer Lawrence.
Jordan, Obamacare Obamacared my Obamacare.
Mike, Obamacare came in with the milk.
Seth, Obamacare came and took mah baby... MAH BABY.
Mike, Obamacare stole mah story.Mike McNeely's photo.
Mike, Obamacare is burning down Hot Springs for more parking lots!
Seth, Obamacare sent me intensely sexual private messages.
Mike, Obamacare brainwashed the Arkansas senate.
Mike, Obamacare plans to picket Fred Phelps' funeral.
Mike, Obamacare asked me to look at the flowers.
Seth, Obamacare downgraded my internet speed.
Mike, Obamacare let it go, let it go, the cold never bothered it anyway.
Greg, Obamacare POOPED MY
Mike, Obamacare is slowly removing Greg's hair.
Greg, Obamacare is a
Greg, Obamacare drank all the milks and now I cant eat pancakes.
Mike, Obamacare won't let that kid take his My Little Pony backpack to school.
Greg, Obamacare smeared poop in your wifes eye and gave her the pink eyes.
Mike, Obamacare didn't wear green on St Patty's Day and acted like a bitch when everyone tried to pinch it.
Mike, Obamacare is breeding spiders under Kevin's house.
Kevin, Obamacare peed in the floor while I was distracted!
Mike, Obamacare unnecessarily padded those damn Hobbit movies.
Greg, Obamacare didnt make those Hobbit movies long enough in my
Mike, Obamacare called you a Hobbit-apologist.
Greg, Obamacare will help those who have such views to get over
Mike, Obamacare did away with the expanded universe.
Greg, Obamacare said only the movies were canon and everything else had to be burned.
Mike, Obamacare all along!
Greg, Obamacare backwards it would slowly say Hail Hydra.
Mike, Obamacare cast Channing Tatum in a Gambit movie.
Greg, Obamacare made peoples expectations for movies these days to be too high.
Mike, Obamacare gives away the entire movie in the trailers.
Mike, Obamacare that matters, it's how you use it.
Lenny, Obamacare sent me a lovely Birthday card and a free sample of Soylent Green.
Kevin, Obamacare is people!
Mike, Obamacare ate all of the Doritos.
Greg, Obamacare is waging a hidden war across the planet, eith JSOC and Admiral McRaven as it's head.
Mike, Obamacare is that coworker who can't go a day without talking shit about whomever isn't present.
Mike, Obamacare should get me a good job at the Arlington.
Greg, Obamacare gaveme the aids.
Mike, Obamacare gave ME assistants.
Greg, Obamacare just became aware of this thread.
Mike, Obamacare is cover us up Benghazi style.
Mike, Obamacare gave Kitty Pryde time travel powers.
Greg, Obamacare is why Iceman is the most powerful mutant in existance.
Mike, Obamacare drank all of my crack cocaine
Casey, Obamacare cut in my line at the grocery store with 3 items instead of using the express checkout.
Greg, Obamacare took out Buenos Aires with a bug meteor. Nothing lives in once what once called the Latin Paradise. Buenos Aires has been wiped off the Earth. The Federal Council met moments ago and voted unanimously for authorization to destroy the bug threat.13 hours ago
Lenny, Obamacare's favorite movies are "To Wong Foo", "Tango & Cash", and "Lethal Weapon 3".
Casey, Obamacare wears mirrored sunglasses to no-stakes poker games amongst friends.
"""