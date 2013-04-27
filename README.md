<h1>Digin (Working Title) (also: Shovel Party)</h1>
<h3>
A competitive card game for you and your friends!
</h3>
<h2>
There are 8 characters:
</h2>
<ul>
<li>Billy the Lumberjack
<li>Sandy the Vampire
<li>Joe the Normal guy
<li>A1 the steak sauce Robot
<li>Lily the sneaky Thief
<li>Steve the gambling Jester
<li>Amy the gold-digger 
<li>Greg the scariest Ghost
</ul>


<h2>
They each have 1 unique ability:
</h2>
<ul>
<li>Billy can equip two things
<li>Sandy can take a card from the graveyard
<li>Joe can shuffle the map (maybe fill holes)
<li>A1 can use a players equipment on them.
<li>Lily can steal any non-coin card from a players hand
<li>Steve can switch hands with a player
<li>Amy can steal any coin from a players hand
<li>Greg can teleport to any place on the map
</ul>
Abilities must be unlocked by using an ability card from your hand.
(ability cards work like a stack in magic "FIFO")

<h2>
Game-play:
</h2>
The objective of the game is to collect the most gold before the set amount of turns. (Average amount of turns is 20)
You can also win by killing the other players. You die when you have no more cards besides your character card. (This includes the cards in your hand and your equipment)
Everyone has a hand of cards and there is a field of cards called the Map.

<h2>
The Set Up:
</h2>
To start the game, you take a bunch of cards that you like and shuffle them in a pile. 
<p>This will be the Map.
<p>Each player begins the game with their character card on the field in a fair space in front of them. Each player also begins with their hand consisting of 1 bomb card, and 3 coins and 1 rock.
<p>Each player rolls to see who goes first and the turn order is set from there.

<h3>
A typical turn consists of
</h3>
If you have any cards you would like to equip to your character , you may do so.
Only 1 equipment at a time. You can also unequip stuff during this phase.
(When you do you take the card that was on your character already, if there was one, and put it in your hand)
You roll the die.
(If a character has whiskey, he/she moves now and can look at the card they land on)
You move your character card the appropriate amount of spaces in any direction (north, south, east or west) except diagonally. 
You can then look at the Map card that you land on, do what it says (the pick-up effect) and take the card and swap it with one in your hand (including that card)
You don't have to look at the card you land on.
If you land on a space where someone already occupies:
you "use" your equipment card on them.

<h2>
Card Types:
</h2>

<h3>Gold Cards</h3> - Gold cards are the basic monetary points in the game and can be equipped. (They do nothing when equipped)

<h3>Supplies Cards</h3> - Supplies cards are any card that aren't a coin or artifact. 
There is 3 types: Offensive, Defensive, and Support.

<h3>Artifact Cards</h3> - Artifact cards count as both a coin and a supply card.


<h2>
Supplies Card Types:
</h2>

<h3>Offensive</h3> - Activates when your character lands on a space where another character occupies.

<h3>Defensive</h3> - Activates when an opponent lands on the space that your character occupies.

<h3>Support</h3> - Activates whenever you land anywhere.


<h2>
The Cards:
</h2>

woman's purse - show your hand to someone,
equip: look at players hand and take 1 coin


bomb - discard a card and don't put a card back in the map,
equip: make player discard a card, then discard the bomb (on opp's turn only)

sword - do nothing,
equip: make them opponent discard equipment card

Magic Frog - if you have the flag, you have to swap it for this
(if you have an ability card you must put it down and change the frog to a show card)
equip: look at players hand and make them use the pickup (maybe any ability) ability of one of their cards

dirt pile - do nothing,
equip: do nothing.

rock - you trip and discard your equipment
equip: do nothing

ability - Use once by discarding 
(get a dirt pile in it's place)

flag - discard this card to end the game

runnin' boots - do nothing,
equip: take 2 turns if you land on a player
(can be used for an infinite combo)

gum - dont move next turn,
equip: opponent doesnt move next turn
(idk if i like this)

maybe a slippery item?
(maybe not)


shovel - too good?
HAVE TO SHOW THE CARD YOU GET

gold doubloons - points?
TWO TYPES - 1's and 3's (START OUT WITH 3: 1's)

a shop item (equip to set up a shop)
(the challenge is how to make people not attack you and shop instead but not make it too OP) PUT SHOP BACK FACE-UP AND WHEN PEOPLE LAND ON IT THEY "SHOP" WITH YOU

whiskey - carry it around to move on other peoples turns

dark shovel - take from graveyard
(set back is you have to discard all non-coins)

some sort of detective item that lets you look at the cards before you pick them up at no cost?

a wallet (or treasure chest)
get a coin from the graveyard when you pick it up
equip: give a coin to player

3 valuable artifacts
equip effects:

take a card from a player's hand

use your ability

take a players turn (too powerful)

<h2>
Tester
</h2>
(write in python)
<h3><p>
must include:
</h3>
<ul>
<li>computers that play through the game (easy, med, hard)
<li>the cards and a way to add new cards
<li>match stats ( turns it took, a log of each turn)
</ul>
<h3><p>
Classes:
</h3>
<ul>
<li>player - ability
<li>card - 2 effects
<li>map - cards in map (grid)
<li>deck - cards in the deck (total)
<li>hand - cards in a players hand
</ul>




<h2>
ISSUES / FIXES:
</h2>
<h3>
April 19, 2013
</h3>
<ul>
<li>shovel OP
<li>bombs too good if they last forever
<li>too difficult
</ul>
<h3>
April 20, 2013
</h3>
<ul>
<li>shovel fixed
<li>bombs better if they go off and you discard (and destroy the land) and then if you equip they are used as defense
<li>bombs can't kill someone (if you have one card and you land on a bomb you discard a card and then pick up the bomb...NEEDS FIXING)

<li>Should ability cards give you dirt piles when you use them?

<li>discarding the flag is too difficult
(catapult helps? not sure)
(perhaps the flag goes back face-up)
<li>It felt weird changing focus from collecting gold to trying to figure out how to discard the flag
(maybe multiple flags?)

<li>changed running boots (maybe too good now? we'll see)
<li>detective item idea
<li>discard from the map idea
<li>give a card to a player idea
</ul>
<h3>
April 23, 2013
</h3>
<ul>
<li>maybe change the coins to artifacts and they are archeologists digging for the pieces and when you get all of them its like super powerful?
(it's time to introduce some back-story to the game)
<li>seriously considering getting rid of the flag
<li>instruments?
</ul>
<h3>
April 24, 2013
</h3>
<ul>
<li>ability cards need to be "exiled" otherwise Sandy infinite dirt combo happens.
<li>Amy's ability needs to be only the hand
<li>change shop to trading post and you can exchange goods in team play
(maybe add random cards to sell)
<li>woman's purse only takes a coin from hand
<li>bomb blows up hand or equip (you don't choose though)
<li>maybe the game can come with a grid - pad to draw out the map (so you can learn the lay of the land)
(it would make joe better)
<li>equip card face-up in front of you (instead of under character card)
</ul>
<h3>
April 26, 2013
</h3>
<ul>
<li>Ability cards only exiled when used.
<li>thinking about fixing catapult and shop and shovel.
<li>thinking about expansion packs (booster packs with extra cards that you can add to your Map and games)
<li>thinking about new characters (possibly a man with his dog, the ability can be a 2nd character to move around!!!!)
<li>thinking about pets/ instruments
</ul>
