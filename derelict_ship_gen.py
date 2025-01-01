"""
DERELICT SHIP GENERATOR (Skeleton)

Full of quotes from your conversation so you can remember your ideas.
Keep in mind this is just a rough framework—you'll flesh it out as needed.
"""


########################################
# 1. INTRODUCTION & USER QUOTES
########################################

# "New mothership campaign. Talk to me about derelict ships. 
#  We are going high level right now, don't get bogged down in specifics 
#  or try to generate one. We are talking mechanically how I would run 
#  a game of mothership based on the idea of derelict ships."

# "Based on the materials, let me break down how I'd approach running 
#  a Mothership campaign centered around derelict ships:
#  
#  1) SHIP GENERATION
#     Dead Planet provides a fantastic derelict ship generator system 
#     focused on flowchart-style mapping with 6-sided dice...
#  
#  2) SURVIVAL MECHANICS
#     The key survival elements to track: Oxygen supply... 
#     (etc. enumerating resources, hazards) 
#  
#  3) INVESTIGATION FLOW
#     Structure investigations as: initial scans, careful entry, 
#     room-by-room exploration...
#  
#  4) ENCOUNTER DESIGN
#     Layer different threat types: environmental, biological, 
#     psychological, technical, human...
#  
#  5) REWARDS & CONSEQUENCES
#     Balance risk/reward with salvage, scientific discoveries, 
#     contamination risks, psychological trauma..."
#  
# "I have an idea where I generate the rooms with Stable Diffusion live 
#  as they explore. I just have to stay one room ahead of them, 
#  I can make anything the book can come up with and I can do it infinitely."

# "This is a brilliant application of AI image generation for Mothership!
#  Let me break down why this works particularly well:
#  
#   - REACTIVE GENERATION: you only need to generate rooms as players discover them...
#   - HORROR ENHANCEMENT: slight uncanniness of AI generation works in your favor...
#   - PRACTICAL ADVANTAGES: no need to pre-gen entire ship, adapt to player choices..."
#  
# "I can control the layout of the rooms using controlnets, 
#  so a room will have doors where it needs to have doors. 
#  That way I can keep things somewhat consistent."
#  
# "That's an excellent technical solution! ... 
#  The key is making each derelict feel unique and dangerous while maintaining 
#  that core tension between survival and salvage opportunity."
#  
# "I can work on the prompts in advance, I have a list of all possible rooms, 
#  I can find prompts that generate the kinds of spaces we're looking for. 
#  There are only so many types of rooms. Can you list them?"
#  
# "Looking at the derelict ship module generator from Dead Planet, 
#  here are the core room types you'd need prompts for:
#  
#   ESSENTIAL SHIP ROOMS: Command/Bridge/Cockpit, Jump Drive Room, 
#   Life Support Systems, Thrusters/Engine Room, Cargo Holds...
#  
#   SPECIALIZED ROOMS: Medical Bay, Science Labs, Cryochamber...
#  
#   CONNECTING SPACES: Corridors, Maintenance Shafts, Elevator Areas...
#  
#  For each, you'd want variations: pristine, damaged, destroyed, etc."
#  
# "The goal is to be able to stick 'em together like mad-libs. 
#  Maybe even give it some sort of UI, could automate the whole thing... 
#  It's a simple dictionary lookup, a python script could generate 
#  an entire ship and output the prompt for each room."

# "This is a great idea for automation! 
#  Let me sketch out how this could work as a system: 
#  
#   BASE COMPONENTS (python dictionaries for room_types, conditions, etc.)
#   Generate a ship layout using Dead Planet's system 
#   For each room, randomly select condition/lighting/detail 
#   Output complete ControlNet-ready prompts..."

# "And I can modify the future prompts live as we play, 
#  altering the images in advance before they get there."

# "Exactly! This gives you dynamic control over the horror progression 
#  and narrative pacing..."

# "Okay. That's it. No more features. Box it up, gimme an outline of the idea."

# "DERELICT SHIP GENERATOR WITH LIVE AI IMAGING:
#  
#  1) Generate derelict ship rooms in real-time 
#     using Stable Diffusion + ControlNet
#  
#  2) ControlNet ensures architectural consistency
#  
#  3) Stay one room ahead of player exploration
#  
#  4) Keep it simple, flexible, infinitely expandable. 
#     The power is in focusing on one room at a time 
#     rather than pre-generating everything."

# "Okay. Our program does not generate the images. I will do that in Krita. 
#  Our program generates ships and prompts. I want to be able to feed it a prefix, 
#  like 'Alien infested' but otherwise it's a simple lookup system. 
#  There are only 60 options here and a lot of them are duplicates. 
#  No lookup table, we'll just hardwire each one, 
#  the current descriptions wouldn't be valuable for generation anyway."

# "The map is non-trivial."

# "Ah yes - you're right. The map generation is actually the complex part here. 
#  Looking at Dead Planet's system:
#  You literally just: Drop dice on a page, number them 1-10, connect them with lines...
#  Hidden ducts can be created by connecting rooms whose numbers add to 7.
#  It's not about making logical, navigable spaces - it's about weird, horrific environments."

# "Exactly. I believe it should be, given x squares, 
#  make an interesting arrangement out of them."

# "This hangs on whether we can make interesting geometries. 
#  As long as the squares touch the spaces will be navigatable, 
#  what we need is the kind of geometries a human cannot do. 
#  Gimme some fun math that makes cool shapes."

# "Conway is too small, It needs to form clumps and strings,"

# "No, that's not what we want, we want X's and 8's symmetry, 
#  or purposeful looking asymmetry."

# "Do you see anything in this book that implies the ship has to be any of those things?
#  This system generates nonsense ships, so will ours. We aren't changing the game."

# "We should keep that same spirit—generate weird configurations 
#  and embrace the chaos rather than trying to enforce logic on it."

# "AH! Now I understand - we want architectural patterns, 
#  not organic ones. We want things that look purposefully designed 
#  with symmetrical crosses (X shapes), figure-8 patterns, 
#  or deliberate asymmetry that still feels engineered."



########################################
# 2. SKELETON CODE OUTLINE
########################################

def generate_ship_layout(num_rooms=10):
    """
    Generate a random map of 'num_rooms' rooms.

    "We can either do the Dead Planet dice-drop method (i.e. nonsense),
     or code something for symmetrical shapes (X's, 8's) 
     that look 'purposeful'."
    """

    # Pseudocode / placeholders:
    # 1) Possibly pick a "pattern" at random (like X-shaped, figure-8, simple grid).
    # 2) Place squares (rooms) in that pattern.
    # 3) Number them 1..num_rooms.
    # 4) Connect them with lines in some interesting way (maybe random or symmetrical).
    # 5) Return a data structure that has:
    #    - Each room's name or index
    #    - Connections to other rooms (adjacency list)
    #    - Possibly some random "prefix" or "detail" to each
    pass


def generate_room_prompts(ship_layout, prefix=None):
    """
    Given a 'ship_layout' (the result of generate_ship_layout),
    produce text prompts for each room.

    "No lookup table, we'll just hardwire each one, the current 
     descriptions wouldn't be valuable for generation anyway. 
     I want to feed it a prefix, like 'Alien infested.'"
    """

    # Pseudocode example:
    # for each room in ship_layout:
    #    base_description = "Bridge" or "Engine Room" etc.
    #    final_prompt = f"{prefix} {base_description} with some descriptors..."
    #    store prompts in a dictionary or list
    # return the dictionary/list
    pass


def main():
    """
    Main flow:
    1) Generate random ship layout (which could be nonsense or symmetrical).
    2) Generate the text prompts for each room (with optional prefix).
    3) Print or save the results for usage in Krita/Stable Diffusion.

    "And I can modify the future prompts live as we play, 
     altering the images in advance before they get there."
    """
    # Example usage:
    # layout = generate_ship_layout(num_rooms=10)
    # prompts = generate_room_prompts(layout, prefix="Alien Infested")
    # for room_num, prompt in prompts.items():
    #     print(f"Room {room_num}: {prompt}")
    pass


########################################
# 3. FURTHER NOTES / TO-DO
########################################

# "The real art is how we produce the MAP. It's okay if it's nonsense, 
#  but we might also want symmetrical or near-symmetrical shapes. 
#  'We want X's and 8's symmetry, or purposeful looking asymmetry.'"

# "Our program does not generate the images. I will do that in Krita. 
#  Our program generates ships and prompts."

# "Remember: We want to keep that Dead Planet vibe: 
#  'Hidden ducts can be created by simply connecting rooms 
#   whose numbers add up to 7.' 
#  It's a weird, horrifying environment."

# "We can incorporate special triggers or details if we want: 
#  e.g. 'When the players open this door, add a clue about infestation 
#  into the next room's prompt.' 
#  'If they damage life support, add a prefix like "power failing" 
#  to all subsequent prompts.' 
#  This is the advantage of generating it live."

# "As you said: 'The power is in focusing on one room at a time 
#   rather than trying to pre-generate everything.' 
#  We'll just keep it agile, make it up as we go."

# -- END OF PROGRAM SKELETON --
