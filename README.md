<h1>Digin</h1>
V.1.9
<h3>
A competitive card game for you and your friends!
</h3>
<h2>
There are 8 characters:
</h2>
<ul>
<li><bold>Billy</bold> the Lumberjack
<li><bold>Sandy</bold> the Vampire
<li><bold>Joe</bold> the Normal guy
<li><bold>A1</bold> the steak sauce Robot
<li><bold>Lily</bold> the sneaky Thief
<li><bold>Steve</bold> the gambling Jester
<li><bold>Amy</bold> the gold-digger 
<li><bold>Greg</bold> the scariest Ghost
</ul>


<h2>
They each have 1 unique ability:
</h2>
<ul>
<li><bold>Billy</bold> can equip two things (equip another item)
<li><bold>Sandy</bold> can take a card from the graveyard
<li><bold>Joe</bold> can shuffle the map (maybe fill holes)
<li><bold>A1</bold> can use a players equipment on them.
<li><bold>Lily</bold> can steal any non-coin card from a players hand
<li><bold>Steve</bold> can switch hands with a player
<li><bold>Amy</bold> can steal any coin from a players hand
<li><bold>Greg</bold> can teleport to any place on the map
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
<br>This will be the Map.
<br>Each player begins the game with their character card on the field in a fair space in front of them. 
<br>Each player also begins with their hand consisting of 1 bomb card, and 3 coins and 1 rock.
<br>Each player rolls to see who goes first and the turn order is set from there.

<h3>
A typical turn consists of
</h3>
<ul>
<li>If you have any cards you would like to equip to your character, you may do so.
<br>Only 1 equipment at a time. You can also unequip stuff during this phase.
<br>(When you do you take the card that was on your character already, if there was one, and put it in your hand)
<li>You roll the die.
<br>(If a character has whiskey, he/she moves now and can look at the card they land on)
<li>You move your character card the appropriate amount of spaces in any direction (north, south, east or west) except diagonally. 
<li>You can then look at the Map card that you land on, do what it says (the pick-up effect) and take the card and swap it with one in your hand 
<br>(including that card)
<li>You don't have to look at the card you land on.
<li>If you land on a space where someone already occupies you can use your Offensive equipment card on them. (If more than one person occupies a space the Offensive Equipment activates on everyone on that space.)
</ul>

<h3>
A card consists of
</h3>
<ul>
<li>The type of card it is
<li>A picture of whatever it is
<li>The Cards Pick-Up effect
<li>The Cards Equip effect
<li>A quote/flavor text
</ul>

<h2>
Card Types:
</h2>

<h3>Gold Cards</h3> - Gold cards are the basic monetary points in the game and can be equipped. (They do nothing when equipped)

<h3>Supplies Cards</h3> - Supplies cards are any card that aren't gold or artifact. (They have no point values) 
There is 3 types: Offensive, Defensive, and Support.

<h3>Artifact Cards</h3> - Artifact cards count as both a gold and a supply card.


<h2>
Supplies Card Types:
</h2>

<h3>Offensive</h3> - Activates when your character lands on a space where another character occupies.

<h3>Defensive</h3> - Activates when an opponent lands on the space that your character occupies.

<h3>Support</h3> - Activates whenever you land anywhere.


<h2>
The Cards:
</h2>
<ul>
<li>woman's purse - show your hand to someone,
<br>equip: look at players hand and take 1 coin


<li>bomb - discard a card and don't put a card back in the map,
<br>equip: make player discard a card, then discard the bomb (on opp's turn only)

<li>sword - do nothing,
<br>equip: make them opponent discard equipment card

<li>Magic Frog - if you have an ability, you have to swap it for this
<br>(if you have an ability card you must put it down and change the frog to a show card)
<br>equip: look at players hand and make them use the pickup (maybe any ability) ability of one of their cards

<li>dirt pile - do nothing,
<br>equip: do nothing.

<li>rock - you trip and discard your equipment
<br>equip: do nothing

<li>ability - Use once by discarding 
<br>(get a dirt pile in it's place)

<li>runnin' boots - do nothing,
<br>equip: take 2 turns if you land on a player
<br>(can be used for an infinite combo)

<li>gum - dont move next turn,
<br>equip: opponent doesnt move next turn
<br>(idk if i like this)

<li>shovel - too good?
<br>HAVE TO SHOW THE CARD YOU GET

<li>gold doubloons - points?
<br>TWO TYPES - 1's and 3's (START OUT WITH 3: 1's)

<li>Fools gold
<br>Count's as 2 gold, but if you have it in your hand at the end of the game you have to discard a coin!

<li>a shop item (equip to set up a shop)
<br>(the challenge is how to make people not attack you and shop instead but not make it too OP) 
<br>PUT SHOP BACK FACE-UP AND WHEN PEOPLE LAND ON IT THEY "SHOP" WITH YOU

<li>whiskey - carry it around to move on other peoples turns

<li>dark shovel - take from graveyard
<br>(set back is you have to discard all non-coins)

<li>some sort of detective item that lets you look at the cards before you pick them up at no cost?

<li>a wallet (or treasure chest)
<br>get a coin from the graveyard when you pick it up
<br>equip: give a coin to player

<li>a boat
<br>equip: get over empty spaces(water)
<br>(maybe when you pick it up yu don't put anything down)

<li>3 valuable artifacts
<br>equip effects:
<ul>
<li>take a card from a player's hand

<li>use your ability

<li>take a players turn (too powerful)
</ul>
</ul>
<h2>
Tester
</h2>
(written in Python)
<h3>
Includes:
</h3>
<ul>
<li>computers that play through the game (easy, med, hard)
<li>the cards and a way to add new cards
<li>match stats ( turns it took, a log of each turn)
</ul>
<h3>
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
<li>Notice: shovel OP
<li>Notice: bombs too good if they last forever
<li>Notice: Game too difficult
</ul>
<h3>
April 20, 2013
</h3>
<ul>
<li>Update: shovel fixed
<li>Update: bombs better if they go off and you discard (and destroy the land) and then if you equip they are used as defense
<li>Notice: bombs can't kill someone (if you have one card and you land on a bomb you discard a card and then pick up the bomb...NEEDS FIXING)

<li>Notice: Should ability cards give you dirt piles when you use them?

<li>Notice: discarding the flag is too difficult
(catapult helps? not sure)
(perhaps the flag goes back face-up)
<li>Notice: It felt weird changing focus from collecting gold to trying to figure out how to discard the flag
(maybe multiple flags?)

<li>Update: changed running boots (maybe too good now? we'll see)
<li>Update: detective item idea
<li>Update: discard from the map idea
<li>Update: give a card to a player idea
</ul>
<h3>
April 23, 2013
</h3>
<ul>
<li>Notice: maybe change the coins to artifacts and they are archeologists digging for the pieces and when you get all of them its like super powerful?
(it's time to introduce some back-story to the game)
<li>Notice: seriously considering getting rid of the flag
<li>Notice: instruments?
</ul>
<h3>
April 24, 2013
</h3>
<ul>
<li>Update: ability cards need to be "exiled" otherwise Sandy infinite dirt combo happens.
<li>Update: Amy's ability needs to be only the hand
<li>Update: change shop to trading post and you can exchange goods in team play
(maybe add random cards to sell)
<li>Update: woman's purse only takes a coin from hand
<li>Update: bomb blows up hand or equip (you don't choose though)
<li>Notice: maybe the game can come with a grid - pad to draw out the map (so you can learn the lay of the land)
(it would make joe better)
<li>Notice: equip card face-up in front of you (instead of under character card)
</ul>
<h3>
April 26, 2013
</h3>
<ul>
<li>Update: Ability cards only exiled when used.
<li>Notice: thinking about fixing catapult and shop and shovel.
<li>Notice: thinking about expansion packs (booster packs with extra cards that you can add to your Map and games)
<li>Notice: thinking about new characters (possibly a man with his dog, the ability can be a 2nd character to move around!!!!)
<li>Notice: thinking about pets/ instruments
</ul>
<h3>
April 27, 2013
</h3>
<ul>
<li>Update: Added Names for the different Card Types (offensive, defensive, support)
<li>Update: Equip cards are now called: Supplies cards
<li>Update: Changed coins to gold (Still not sure if I want to keep the coin values 1 and 3 or 1 and 2)
<li>Notice: Thinking about some sort of card that you get to replace an ability card besides dirt?
<li>Notice: change dark shovel to grave shovel?
<li>Update: The old man and his dog:
<br>Use your ability and the dog comes out
<br>The dog has the same equipment that you have
<br>If the dog lands on someone the equipment activates
<br>(if someone lands on the dog, it dies?)
<br>Either you move the dog on your turn or you move it on the turn after you or the turn you summon it.
<li>Update: Turbo Shovel: if you pick-up a dirt pile or coin, you roll again.
</ul>
<h3>
April 29, 2013
</h3>
<ul>
<li>Update: Finished the basics for the Digin Editor
<li>Update: Added working matrix to be used as the map
<li>Notice: The set amount of turns feels pointless in 1v1
<li>Notice: Change dark shovel to (grave, bone, evil)
<li>Notice: Perhaps add another use for money? (buying something)
<li>Notice: Make shovel more appealing
</ul>
<h3>
May 2nd, 2013
</h3>
<ul>
<li>Notice: Add a Facebook page
<li>Notice: Fix "Pure Evil" to make it less powerful
<li>Update: Issues/Fixes section with Tags
<li>Update: Uploaded code for Digin Editor to Github
</ul>
<h3>
May 3rd, 2013
</h3>
<ul>
<li>Update: Fool's Gold!
</ul>
<h3>
May 12th, 2013
</h3>
<ul>
<li>Dark shovel: Show a player your hand and they decide how many non-coin cards to discard
<li>A1 : negates abilities now
<li>Switch abilities so they go to graveyard and Sandy's ability is now: Take a non-ability card from the graveyard
<li>Old Man and Dog - 
<br>Ability: Old man summons dog.
<br>They both share a dice roll (you can divide the roll to each character)
<br>If any player lands on the dog, it goes home and your equipment activates on the man
<br>If the dog lands on any player, the man's equipment activates
<br>(Maybe the old man and dog can swap map cards)
<li>Pure Evil: Deal with the devil, land on a player and discard a coin card to take their next turn
<li>When Joe randomizes the map, he can't make gaps
<li>Highest roll chooses a character first and doesn't show it and then players choose clockwise.
</ul>
<h3>
May 13th, 2013
</h3>
<ul>
<li>Drunk: His ability is he gets a whiskey card
<li>A shield item (defensive)
<li>Switch item with the graveyard
<li>Swap spaces on the map
<li>Dwarf: Pick up the map card you are standing on without doing the pickup ability.
<li>Should the graveyard be face up or face down?
<li>sun tan lotion
<li>More long range items
<li>Medusa's ass cheeks: Choose a random card from the closest player's hand and replace it for dirt. "This part of the myth, I don't remember."
<li>Tino Sniper: If you are playing Never have I ever, one person puts a finger down. 'Niper Spree'
<li> Treasure Chest: "Shutup and take my money!"
<li>Bomb's get priority over other non-ability cards, except sword.
<li>Sword gets priority over every defensive equip.
</ul>
<h3>
August 21, 2013
</h3>
<ul>
<li>"Dig" Cards will be added (in preparation for the Digin 2.0 update)
<li>Removing the 20 turn game limit
<li>The game now ends when all "Dig" cards have been drawn.
<li>"Dig" cards will either be drawn during a players turn, instead of taking their turn, or purchased for a coin price.
<li>Characters now each have a "bounty" depending on how impressive their ability is. 
<br>When you kill this character you get their character card, which now counts as a coin card with a value equal to the bounty value.
<li>Possible theme: A post apocalyptic world, where the characters want to find refuge and are promised riches underground.
<br>(Or maybe something to do with maps, if we change the "Dig" cards to Map cards)
<li>Coin values will have to be altered to reflect these changes.
<li>Character cards will have to be altered to reflect these changes.
<li>Supplies cards will have to be altered to reflect these changes.
<li>Card priority needs to be set
<li>Ability cards need to be re-thought.
<li>Perhaps we get rid of Fool's gold?
<li>Are artifacts necessary?
<li>Card "visibility" should be altered/re-thought. 
<br>(Which cards have eye-balls?, Should all cards be required to be shown?)
</ul>
<h3>
August 22, 2013
</h3>
<ul>
<li>New Character: Assassin
<br>Ability: When you use your ability card, you get a knife equipment (If you currently have an equipment, it gets unequipped to your hand).
<li>Knife:
<br>Equip effects: If you land on a player, throw 2 of their cards into the graveyard.
<br>(The knife can only be equipped by the Assassin or the Shapeshifter when he acts as the Assassin)
<li>(The Knife can't be unequipped by the holder, possibly?)
</ul>


