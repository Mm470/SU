## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:fillers
- [hmmmm](filler)
- [haaaa](filler)
- [mmmm](filler)
- [ehh](filler)
- [ehhhh](filler)
- [ehhh](filler)
- [aaaah](filler)

## intent:identify_location
- [Turn down](verb) the [heat](noun) in [the](splitpoint)
- [Turn up](verb) the [heat](noun) in [the](splitpoint)
- [Increase](verb) the [heat](noun) in [the](splitpoint)
- [Decrease](verb) the [heat](noun) in [the](splitpoint)
- [Turn down](verb) the [music](noun) in [the](splitpoint)
- [Turn up](verb) the [music](noun) in [the](splitpoint)
- [Increase](verb) the [music](noun) in [the](splitpoint)
- [Decrease](verb) the [music](noun) in [the](splitpoint)
- [Turn](verb) the [temperature](noun) [down](verb) [in the](splitpoint)

## intent:filler_sentence1_heating
- [Decrease](verb) [the](splitpoint)
- Could you [decrease](verb) [the](splitpoint)
- [Decrease](verb) in [the](splitpoint) [living room](location)
- [Decrease](verb) [mmmm](filler) in the [living room](location)
- [Turn the](verb) [ehhh](filler) down [in the](splitpoint) living room
- [Turn down](verb) the [haaaa](filler) in the living room
- living room [ehh](filler)
- Increase [the](splitpoint)
- Could you [increase](verb) [the](splitpoint)
- Could you please [increase](verb) [the](splitpoint)
- Make it hotter[ehhh](filler)
- [Decrease](verb) [mmmm](filler) in the living room
- living room [mmmm](filler)
- Make it hotter [mmmm](filler)
- [Increase](verb) [the](splitpoint)

## intent:filler_sentence2_music
- can you [turn on](verb) [my](splitpoint)
- can you [turn down](verb) [the](splitpoint)
- Make [the](splitpoint)
- [Turn down](verb) [the](splitpoint)
- [Make](verb) [the](splitpoint)
- [Turn off](verb) [the](splitpoint)
- [Stop](verb) [the](splitpoint)
- [Play](verb)
- [Put on](verb) [the](splitpoint)
- [Play](verb) [the](splitpoint)
- [Start](verb) [the](splitpoint)

## intent:filler_sentence3_lights
- Switch [the](splitpoint) [mmmm](filler) on
- [Switch on](verb) [the](splitpoint) [living room](location)
- Switch [the](splitpoint) [mmmm](filler) off
- [Switch off](verb) [the](splitpoint) [living room](location)
- [Switch on](verb) [the](splitpoint)
- switch on [the](splitpoint) [living room](location)
- switch [the](splitpoint) [mmmm](filler) off
- switch [the](splitpoint) [mmmm](filler) on
- [Switch on](verb) [the](splitpoint) [mmmm](filler)
- switch off [the](splitpoint) [living room](location)
- Switch [the](splitpoint) [hmmmm](filler) off

## intent:filler_sentence5
- please switch on [hmmmm](filler)
- please switch on [ehh](filler)
- please switch on [haaaa](filler)

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:filler_sentence4_tv
- I need to [hear](verb) this, [increase](verb) the volume
- I couldn't [hear](verb) anything, [increase](verb) the volume
- I can't [hear](verb) that
- Too [quiet](silent)
- [Turn the](verb) sound up
- [Turn sound](verb) down
- [Decrease](verb) audio volume
- This [video](noun) sound is too low, [turn up](verb) the volume
- I need to see this, turn the volume
- [quieter](silent)
- Too [quiet](silent)
- [quieter](silent)
- I can't [hear](verb) that
- I need to [hear](verb) this [increase](verb) the volume
- I couldn't [hear](verb) anything, [increase](verb) the volume
- [Turn the](verb) sound up
- [Decrease](verb) audio volume

## lookup:location
- living room
- Living Room
- living area
- Living area
- Living Area

## lookup:splitpoint
- my
- the
- a
- to
- in

## lookup:silent_intent
- quiet
- quieter
- silent
- silence

## lookup:verb
- turn on
- turn down
- call
- need
- start
- play
- want
- turn
- down
- up

## lookup:noun
- oven
- light
- heating
- heat
- music
- tv

## lookup:filler
- hmmmm
- haaaa
- mmmm
- ehh
- ehhhh
- ehhh
- aaaah
