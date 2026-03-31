#!/usr/bin/env python3
"""Generate Clawd icon set based on Claude Code mascot."""

import os

BASE_PATH = 'M20.998 10.949H24v3.102h-3v3.028h-1.487V20H18v-2.921h-1.487V20H15v-2.921H9V20H7.488v-2.921H6V20H4.487v-2.921H3V14.05H0V10.95h3V5h17.998v5.949zM6 10.949h1.488V8.102H6v2.847zm10.51 0H18V8.102h-1.49v2.847z'

BLUE = '#5B9BD5'
GREEN = '#6BBF6B'
YELLOW = '#F0C75E'
RED = '#E05252'
MASCOT = '#D97757'
WHITE = '#FFFFFF'
DARK = '#3A3A3A'

def svg(title, indicator, transform="translate(4,24) scale(4)"):
    return f'''<svg width="128" height="128" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">
  <title>{title}</title>
  <g transform="{transform}">
    <path clip-rule="evenodd" d="{BASE_PATH}" fill="{MASCOT}" fill-rule="evenodd"/>
  </g>
{indicator}
</svg>
'''

# --- TOOL ICONS (Blue) ---

icons = {}

# Read - document with lines
icons['clawd_read'] = svg('Read File', f'''  <rect x="84" y="2" width="40" height="44" rx="4" fill="{BLUE}"/>
  <rect x="92" y="12" width="24" height="4" fill="{WHITE}"/>
  <rect x="92" y="20" width="24" height="4" fill="{WHITE}"/>
  <rect x="92" y="28" width="16" height="4" fill="{WHITE}"/>
  <rect x="92" y="36" width="20" height="4" fill="{WHITE}"/>''')

# Edit - pencil
icons['clawd_edit'] = svg('Edit File', f'''  <g transform="translate(88,2)">
    <rect x="8" y="0" width="8" height="8" fill="{BLUE}"/>
    <rect x="4" y="8" width="8" height="8" fill="{BLUE}"/>
    <rect x="0" y="16" width="8" height="8" fill="{BLUE}"/>
    <rect x="0" y="24" width="4" height="8" fill="{BLUE}"/>
    <rect x="24" y="0" width="8" height="8" fill="{BLUE}"/>
    <rect x="20" y="8" width="8" height="8" fill="{BLUE}"/>
    <rect x="16" y="16" width="8" height="8" fill="{BLUE}"/>
    <rect x="12" y="24" width="4" height="4" fill="{BLUE}"/>
    <rect x="12" y="8" width="8" height="8" fill="{WHITE}" opacity="0.3"/>
  </g>''')

# Write - document top-right + pen in right hand
icons['clawd_write'] = svg('Write File', f'''  <!-- document badge -->
  <rect x="86" y="2" width="36" height="40" rx="3" fill="{BLUE}"/>
  <rect x="92" y="10" width="24" height="3" fill="{WHITE}"/>
  <rect x="92" y="17" width="24" height="3" fill="{WHITE}"/>
  <rect x="92" y="24" width="16" height="3" fill="{WHITE}"/>
  <rect x="92" y="31" width="20" height="3" fill="{WHITE}"/>
  <!-- pen in right hand -->
  <line x1="100" y1="76" x2="118" y2="52" stroke="{YELLOW}" stroke-width="4" stroke-linecap="round"/>
  <line x1="118" y1="52" x2="120" y2="48" stroke="{DARK}" stroke-width="3" stroke-linecap="round"/>''')

# Bash - terminal >_
icons['clawd_bash'] = svg('Bash Terminal', f'''  <rect x="80" y="2" width="46" height="40" rx="4" fill="{DARK}"/>
  <rect x="80" y="2" width="46" height="10" rx="4" fill="{BLUE}"/>
  <rect x="88" y="18" width="4" height="4" fill="{GREEN}"/>
  <rect x="92" y="22" width="4" height="4" fill="{GREEN}"/>
  <rect x="96" y="26" width="4" height="4" fill="{GREEN}"/>
  <rect x="104" y="30" width="12" height="4" fill="{WHITE}"/>''')

# Glob - folder top-right + magnifying glass in right hand
icons['clawd_glob'] = svg('Glob Search', f'''  <!-- folder badge top-right -->
  <rect x="86" y="2" width="28" height="20" rx="2" fill="{YELLOW}"/>
  <rect x="86" y="2" width="14" height="7" rx="2" fill="{YELLOW}" stroke="#d4a840" stroke-width="1"/>
  <!-- magnifying glass: handle in right hand, lens up-right (smaller) -->
  <line x1="100" y1="76" x2="107" y2="66" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>
  <circle cx="112" cy="58" r="9" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <circle cx="112" cy="58" r="3" fill="{BLUE}" opacity="0.1"/>''')

# Grep - text highlight top-right + magnifying glass in right hand
icons['clawd_grep'] = svg('Grep Search', f'''  <!-- text lines badge top-right -->
  <rect x="84" y="4" width="30" height="3" fill="{BLUE}" opacity="0.4"/>
  <rect x="84" y="11" width="26" height="3" fill="{YELLOW}"/>
  <rect x="84" y="18" width="30" height="3" fill="{BLUE}" opacity="0.4"/>
  <rect x="84" y="25" width="22" height="3" fill="{BLUE}" opacity="0.4"/>
  <!-- magnifying glass: handle in right hand, lens up-right (smaller) -->
  <line x1="100" y1="76" x2="107" y2="66" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>
  <circle cx="112" cy="58" r="9" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <circle cx="112" cy="58" r="3" fill="{BLUE}" opacity="0.1"/>''')

# LSP - code brackets </>
icons['clawd_lsp'] = svg('LSP Code Intelligence', f'''  <g fill="{BLUE}">
    <rect x="84" y="10" width="4" height="4"/>
    <rect x="80" y="14" width="4" height="4"/>
    <rect x="76" y="18" width="4" height="4"/>
    <rect x="80" y="22" width="4" height="4"/>
    <rect x="84" y="26" width="4" height="4"/>
    <rect x="96" y="16" width="4" height="4"/>
    <rect x="100" y="20" width="4" height="4"/>
    <rect x="112" y="10" width="4" height="4"/>
    <rect x="116" y="14" width="4" height="4"/>
    <rect x="120" y="18" width="4" height="4"/>
    <rect x="116" y="22" width="4" height="4"/>
    <rect x="112" y="26" width="4" height="4"/>
  </g>''')

# WebFetch - globe + clean download arrow
icons['clawd_webfetch'] = svg('Web Fetch', f'''  <!-- globe -->
  <circle cx="100" cy="16" r="14" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <line x1="86" y1="16" x2="114" y2="16" stroke="{BLUE}" stroke-width="2"/>
  <line x1="100" y1="2" x2="100" y2="30" stroke="{BLUE}" stroke-width="2"/>
  <ellipse cx="100" cy="16" rx="6" ry="14" fill="none" stroke="{BLUE}" stroke-width="2"/>
  <!-- download arrow (clean) -->
  <line x1="116" y1="24" x2="116" y2="44" stroke="{GREEN}" stroke-width="4" stroke-linecap="round"/>
  <polyline points="108,36 116,44 124,36" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="106" y1="48" x2="126" y2="48" stroke="{GREEN}" stroke-width="3" stroke-linecap="round"/>''')

# WebSearch - globe top-right + magnifying glass in right hand
icons['clawd_websearch'] = svg('Web Search', f'''  <!-- globe badge top-right -->
  <circle cx="100" cy="18" r="14" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <line x1="86" y1="18" x2="114" y2="18" stroke="{BLUE}" stroke-width="2"/>
  <line x1="100" y1="4" x2="100" y2="32" stroke="{BLUE}" stroke-width="2"/>
  <ellipse cx="100" cy="18" rx="6" ry="14" fill="none" stroke="{BLUE}" stroke-width="2"/>
  <!-- magnifying glass: handle in right hand, lens up-right (smaller) -->
  <line x1="100" y1="76" x2="107" y2="66" stroke="{YELLOW}" stroke-width="3" stroke-linecap="round"/>
  <circle cx="112" cy="58" r="9" fill="none" stroke="{YELLOW}" stroke-width="3"/>
  <circle cx="112" cy="58" r="3" fill="{YELLOW}" opacity="0.1"/>''')

# Notebook - Jupyter-style notebook with code cells + pen in hand
icons['clawd_notebook'] = svg('Notebook Edit', f'''  <!-- notebook body -->
  <rect x="86" y="2" width="38" height="44" rx="3" fill="{DARK}"/>
  <!-- code cell 1 (with In[] marker) -->
  <rect x="90" y="6" width="4" height="10" rx="1" fill="{BLUE}"/>
  <rect x="96" y="6" width="24" height="10" rx="1" fill="#2a2a3a"/>
  <rect x="98" y="9" width="14" height="2" fill="{GREEN}" opacity="0.7"/>
  <rect x="98" y="13" width="10" height="2" fill="{GREEN}" opacity="0.5"/>
  <!-- code cell 2 -->
  <rect x="90" y="20" width="4" height="10" rx="1" fill="{BLUE}"/>
  <rect x="96" y="20" width="24" height="10" rx="1" fill="#2a2a3a"/>
  <rect x="98" y="23" width="16" height="2" fill="{YELLOW}" opacity="0.7"/>
  <rect x="98" y="27" width="8" height="2" fill="{YELLOW}" opacity="0.5"/>
  <!-- output cell -->
  <rect x="96" y="34" width="24" height="8" rx="1" fill="#1a1a2a"/>
  <rect x="98" y="37" width="18" height="2" fill="{WHITE}" opacity="0.4"/>
  <!-- pen in right hand -->
  <line x1="100" y1="76" x2="118" y2="52" stroke="{YELLOW}" stroke-width="4" stroke-linecap="round"/>
  <line x1="118" y1="52" x2="120" y2="48" stroke="{DARK}" stroke-width="3" stroke-linecap="round"/>''')

# --- SUBAGENT & STATE ICONS ---

# Agent - mini mascot being spawned with energy lines
icons['clawd_agent'] = svg('Spawn Agent', f'''  <!-- mini mascot (child agent) bouncing out to the right -->
  <g transform="translate(84,6) scale(1.6)">
    <path clip-rule="evenodd" d="{BASE_PATH}" fill="{BLUE}" fill-rule="evenodd"/>
  </g>
  <!-- connection line from parent to child -->
  <path d="M100,72 Q108,56 92,44" fill="none" stroke="{YELLOW}" stroke-width="2" stroke-dasharray="4,3" opacity="0.7"/>
  <!-- energy sparkles around mini mascot -->
  <g fill="{YELLOW}">
    <rect x="82" y="4" width="3" height="3" rx="1"/>
    <rect x="122" y="8" width="4" height="4" rx="1"/>
    <rect x="118" y="38" width="3" height="3" rx="1"/>
    <rect x="80" y="32" width="3" height="3" rx="1"/>
  </g>
  <!-- spawn burst lines -->
  <g stroke="{YELLOW}" stroke-width="2" stroke-linecap="round" opacity="0.5">
    <line x1="78" y1="20" x2="74" y2="16"/>
    <line x1="126" y1="18" x2="128" y2="14"/>
    <line x1="124" y1="36" x2="128" y2="38"/>
  </g>''')

# Explore - mascot holding a flashlight/torch shining right
icons['clawd_explore'] = svg('Explore Codebase', f'''  <!-- flashlight in right hand -->
  <rect x="100" y="66" width="16" height="8" rx="2" fill="{BLUE}"/>
  <rect x="100" y="64" width="6" height="12" rx="1" fill="{BLUE}" opacity="0.8"/>
  <!-- light beam shining right -->
  <polygon points="116,64 128,52 128,88 116,76" fill="{YELLOW}" opacity="0.25"/>
  <polygon points="116,66 126,58 126,82 116,74" fill="{YELLOW}" opacity="0.35"/>
  <!-- light glow at source -->
  <rect x="114" y="66" width="4" height="8" rx="1" fill="{YELLOW}" opacity="0.8"/>''')

# Plan - clipboard with checkmarks
icons['clawd_plan'] = svg('Plan', f'''  <rect x="86" y="0" width="36" height="48" rx="3" fill="{YELLOW}"/>
  <rect x="94" y="-2" width="20" height="8" rx="2" fill="{DARK}"/>
  <rect x="92" y="12" width="4" height="4" fill="{GREEN}"/>
  <rect x="100" y="14" width="16" height="3" fill="{DARK}"/>
  <rect x="92" y="22" width="4" height="4" fill="{GREEN}"/>
  <rect x="100" y="24" width="16" height="3" fill="{DARK}"/>
  <rect x="92" y="32" width="4" height="4" fill="{DARK}" opacity="0.3"/>
  <rect x="100" y="34" width="16" height="3" fill="{DARK}" opacity="0.3"/>''')

# Think - pixel thought bubble with dots
icons['clawd_think'] = svg('Thinking', f'''  <!-- pixel thought bubble -->
  <g fill="{YELLOW}">
    <rect x="40" y="4" width="48" height="4"/>
    <rect x="36" y="8" width="56" height="24"/>
    <rect x="40" y="32" width="48" height="4"/>
    <rect x="56" y="36" width="8" height="4"/>
    <rect x="48" y="40" width="8" height="4"/>
  </g>
  <!-- dots ... -->
  <rect x="48" y="16" width="6" height="6" fill="{DARK}"/>
  <rect x="60" y="16" width="6" height="6" fill="{DARK}"/>
  <rect x="72" y="16" width="6" height="6" fill="{DARK}"/>''')

# Answer - pixel speech bubble with text lines
icons['clawd_answer'] = svg('Answering', f'''  <g fill="{GREEN}">
    <rect x="80" y="4" width="44" height="4"/>
    <rect x="76" y="8" width="52" height="28"/>
    <rect x="80" y="36" width="44" height="4"/>
    <rect x="84" y="40" width="8" height="4"/>
    <rect x="80" y="44" width="8" height="4"/>
  </g>
  <rect x="84" y="12" width="32" height="4" fill="{WHITE}"/>
  <rect x="84" y="20" width="24" height="4" fill="{WHITE}"/>
  <rect x="84" y="28" width="28" height="4" fill="{WHITE}"/>''')

# Ask - pixel question mark bubble
icons['clawd_ask'] = svg('Asking', f'''  <!-- pixel speech bubble -->
  <g fill="{YELLOW}">
    <rect x="80" y="4" width="44" height="4"/>
    <rect x="76" y="8" width="52" height="28"/>
    <rect x="80" y="36" width="44" height="4"/>
    <rect x="84" y="40" width="8" height="4"/>
    <rect x="80" y="44" width="8" height="4"/>
  </g>
  <!-- pixel ? mark -->
  <g fill="{DARK}">
    <rect x="92" y="12" width="16" height="4"/>
    <rect x="108" y="16" width="4" height="8"/>
    <rect x="100" y="24" width="8" height="4"/>
    <rect x="100" y="32" width="4" height="4"/>
  </g>''')

# Wait - hourglass
icons['clawd_wait'] = svg('Waiting', f'''  <g fill="{YELLOW}">
    <rect x="48" y="0" width="32" height="4"/>
    <rect x="52" y="4" width="24" height="4"/>
    <rect x="56" y="8" width="16" height="4"/>
    <rect x="60" y="12" width="8" height="4"/>
    <rect x="56" y="16" width="16" height="4"/>
    <rect x="52" y="20" width="24" height="4"/>
    <rect x="48" y="24" width="32" height="4"/>
  </g>''')

# Error - warning triangle with !
icons['clawd_error'] = svg('Error', f'''  <polygon points="104,2 126,42 82,42" fill="{RED}"/>
  <rect x="101" y="12" width="6" height="16" fill="{WHITE}"/>
  <rect x="101" y="32" width="6" height="6" fill="{WHITE}"/>''')

# --- LIFE ICONS (Green) ---

# Rest - music note floating, relaxed
icons['clawd_rest'] = svg('Resting', f'''  <text x="28" y="24" font-family="serif" font-size="20" fill="{GREEN}">&#9834;</text>
  <text x="56" y="16" font-family="serif" font-size="16" fill="{GREEN}">&#9835;</text>
  <text x="96" y="20" font-family="serif" font-size="24" fill="{GREEN}">&#9833;</text>''')

# Run - mascot tilted forward + spread legs + motion lines (custom pose)
icons['clawd_run'] = f'''<svg width="128" height="128" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">
  <title>Running</title>
  <!-- mascot body tilted forward 12deg -->
  <g transform="translate(28, 12) rotate(12, 52, 60) scale(3.6)">
    <path clip-rule="evenodd" d="{BASE_PATH}" fill="{MASCOT}" fill-rule="evenodd"/>
  </g>
  <!-- extra running legs (overlaid to extend/bend the legs) -->
  <g fill="{MASCOT}">
    <!-- front leg kicking forward -->
    <rect x="36" y="100" width="8" height="8"/>
    <rect x="28" y="104" width="12" height="8"/>
    <!-- back leg kicking back -->
    <rect x="80" y="92" width="8" height="8"/>
    <rect x="84" y="88" width="12" height="8"/>
  </g>
  <!-- motion lines -->
  <g stroke="{GREEN}" stroke-width="3" stroke-linecap="round" opacity="0.6">
    <line x1="2" y1="36" x2="18" y2="36"/>
    <line x1="0" y1="48" x2="22" y2="48"/>
    <line x1="4" y1="60" x2="16" y2="60"/>
    <line x1="2" y1="72" x2="12" y2="72"/>
  </g>
  <!-- dust -->
  <g fill="{GREEN}" opacity="0.3">
    <rect x="90" y="102" width="6" height="6" rx="3"/>
    <rect x="98" y="98" width="4" height="4" rx="2"/>
  </g>
</svg>
'''

# Sleep - normal mascot + sleep cap + ZZZ
icons['clawd_sleep'] = svg('Sleeping', f'''  <!-- sleep cap on head -->
  <rect x="16" y="32" width="72" height="12" rx="4" fill="{BLUE}"/>
  <rect x="16" y="36" width="72" height="8" fill="{BLUE}"/>
  <circle cx="88" cy="28" r="6" fill="{WHITE}"/>
  <!-- ZZZ -->
  <g fill="{BLUE}" font-family="monospace" font-weight="bold">
    <text x="92" y="24" font-size="22">Z</text>
    <text x="106" y="12" font-size="16">Z</text>
    <text x="116" y="4" font-size="12">Z</text>
  </g>''')

# Drink - water glass near right hand
icons['clawd_drink'] = svg('Drinking Water', f'''  <!-- glass near right hand -->
  <rect x="100" y="56" width="24" height="28" fill="{BLUE}" opacity="0.5"/>
  <rect x="100" y="68" width="24" height="16" fill="{BLUE}"/>
  <rect x="100" y="56" width="24" height="4" fill="{BLUE}"/>
  <rect x="104" y="60" width="8" height="6" fill="{WHITE}" opacity="0.3"/>''')

# Eat - bowl with chopsticks near right hand (arm at x=100, y=68-80)
icons['clawd_eat'] = svg('Eating', f'''  <!-- bowl near right hand -->
  <rect x="100" y="72" width="28" height="8" rx="4" fill="{GREEN}"/>
  <rect x="102" y="66" width="24" height="10" rx="6" fill="{GREEN}" opacity="0.8"/>
  <rect x="100" y="76" width="28" height="4" rx="2" fill="#4a9a4a"/>
  <!-- rice/food -->
  <rect x="106" y="64" width="14" height="4" rx="2" fill="{WHITE}"/>
  <!-- chopsticks -->
  <line x1="108" y1="50" x2="112" y2="66" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <line x1="118" y1="50" x2="116" y2="66" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>''')

# Coffee - coffee cup held near right arm (arm extends to x=100, y≈68-80)
icons['clawd_coffee'] = svg('Coffee', f'''  <!-- cup near right hand -->
  <g fill="#8B6C5C">
    <rect x="100" y="60" width="24" height="24"/>
    <rect x="100" y="80" width="24" height="4" fill="#6B4C3C"/>
  </g>
  <!-- handle -->
  <rect x="124" y="64" width="4" height="4" fill="#8B6C5C"/>
  <rect x="124" y="76" width="4" height="4" fill="#8B6C5C"/>
  <rect x="128" y="68" width="4" height="8" fill="#8B6C5C"/>
  <!-- coffee surface -->
  <rect x="104" y="64" width="16" height="4" fill="#6B4C3C"/>
  <!-- steam (pixel) -->
  <g fill="{WHITE}" opacity="0.5">
    <rect x="104" y="52" width="4" height="4"/>
    <rect x="108" y="48" width="4" height="4"/>
    <rect x="104" y="44" width="4" height="4"/>
    <rect x="116" y="52" width="4" height="4"/>
    <rect x="112" y="48" width="4" height="4"/>
    <rect x="116" y="44" width="4" height="4"/>
  </g>''')

# Happy - stars/sparkles around
icons['clawd_happy'] = svg('Happy', f'''  <g fill="{YELLOW}">
    <polygon points="20,8 22,14 28,14 23,18 25,24 20,20 15,24 17,18 12,14 18,14"/>
    <polygon points="108,4 110,8 114,8 111,11 112,15 108,12 104,15 105,11 102,8 106,8"/>
    <polygon points="64,2 65,5 68,5 66,7 67,10 64,8 61,10 62,7 60,5 63,5"/>
  </g>
  <rect x="32" y="60" width="24" height="4" rx="2" fill="#E09070"/>
  <rect x="72" y="60" width="24" height="4" rx="2" fill="#E09070"/>''')

# Sad - tear drop
icons['clawd_sad'] = svg('Sad', f'''  <g fill="{BLUE}" opacity="0.8">
    <ellipse cx="40" cy="78" rx="4" ry="6"/>
    <polygon points="40,68 44,78 36,78"/>
  </g>
  <g fill="{BLUE}" opacity="0.5">
    <ellipse cx="96" cy="82" rx="3" ry="5"/>
    <polygon points="96,74 99,82 93,82"/>
  </g>''')

# Music - headphones aligned to head (head top y=44, sides x=16 and x=88, head center x=52)
icons['clawd_music'] = svg('Listening to Music', f'''  <!-- headband over head top -->
  <path d="M18,56 Q18,36 52,36 Q86,36 86,56" fill="none" stroke="{BLUE}" stroke-width="4"/>
  <!-- ear cups on head sides -->
  <rect x="10" y="52" width="14" height="18" rx="4" fill="{BLUE}"/>
  <rect x="80" y="52" width="14" height="18" rx="4" fill="{BLUE}"/>
  <!-- music notes -->
  <text x="96" y="16" font-family="serif" font-size="18" fill="{GREEN}">&#9835;</text>
  <text x="108" y="8" font-family="serif" font-size="14" fill="{GREEN}">&#9834;</text>''')

# Game - game controller
icons['clawd_game'] = svg('Gaming', f'''  <g transform="translate(78,2)">
    <rect x="0" y="8" width="44" height="28" rx="8" fill="{DARK}"/>
    <rect x="6" y="16" width="4" height="12" fill="{BLUE}"/>
    <rect x="2" y="20" width="12" height="4" fill="{BLUE}"/>
    <circle cx="34" cy="18" r="3" fill="{RED}"/>
    <circle cx="28" cy="24" r="3" fill="{GREEN}"/>
    <rect x="16" y="28" width="4" height="4" rx="1" fill="#666"/>
    <rect x="24" y="28" width="4" height="4" rx="1" fill="#666"/>
  </g>''')

# Read book - open book held in front (between the arms, below head)
icons['clawd_read_book'] = svg('Reading Book', f'''  <!-- open book in front, between arms y=80-104 area -->
  <g transform="translate(14,84)">
    <rect x="0" y="0" width="40" height="24" fill="{GREEN}" rx="2"/>
    <rect x="48" y="0" width="40" height="24" fill="{GREEN}" rx="2"/>
    <rect x="38" y="-2" width="12" height="28" fill="{GREEN}" opacity="0.7"/>
    <!-- text lines -->
    <rect x="4" y="5" width="28" height="2" fill="{WHITE}" opacity="0.5"/>
    <rect x="4" y="10" width="24" height="2" fill="{WHITE}" opacity="0.5"/>
    <rect x="4" y="15" width="28" height="2" fill="{WHITE}" opacity="0.5"/>
    <rect x="54" y="5" width="28" height="2" fill="{WHITE}" opacity="0.5"/>
    <rect x="54" y="10" width="24" height="2" fill="{WHITE}" opacity="0.5"/>
    <rect x="54" y="15" width="28" height="2" fill="{WHITE}" opacity="0.5"/>
  </g>''')

# Wave - hand waving (extending arm)
icons['clawd_wave'] = svg('Waving', f'''  <g fill="{MASCOT}">
    <rect x="112" y="44" width="12" height="12"/>
    <rect x="116" y="32" width="12" height="16"/>
    <rect x="120" y="28" width="8" height="8"/>
    <rect x="116" y="24" width="4" height="8"/>
    <rect x="124" y="24" width="4" height="8"/>
  </g>''')

# === NEW ICONS: Dev Actions ===

# Git - branch icon
icons['clawd_git'] = svg('Git', f'''  <!-- branch lines -->
  <circle cx="96" cy="12" r="5" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <circle cx="116" cy="12" r="5" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <circle cx="106" cy="38" r="5" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <line x1="96" y1="17" x2="106" y2="33" stroke="{BLUE}" stroke-width="3"/>
  <line x1="116" y1="17" x2="106" y2="33" stroke="{BLUE}" stroke-width="3"/>''')

# Debug - bug icon
icons['clawd_debug'] = svg('Debug', f'''  <!-- bug body -->
  <ellipse cx="106" cy="24" rx="10" ry="14" fill="{RED}" opacity="0.85"/>
  <line x1="106" y1="12" x2="106" y2="38" stroke="{DARK}" stroke-width="2"/>
  <line x1="96" y1="20" x2="116" y2="20" stroke="{DARK}" stroke-width="1.5"/>
  <line x1="96" y1="28" x2="116" y2="28" stroke="{DARK}" stroke-width="1.5"/>
  <!-- antennae -->
  <line x1="100" y1="12" x2="96" y2="4" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <line x1="112" y1="12" x2="116" y2="4" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <circle cx="96" cy="4" r="2" fill="{DARK}"/>
  <circle cx="116" cy="4" r="2" fill="{DARK}"/>
  <!-- legs -->
  <line x1="96" y1="18" x2="88" y2="14" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <line x1="96" y1="24" x2="88" y2="24" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <line x1="96" y1="30" x2="88" y2="34" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <line x1="116" y1="18" x2="124" y2="14" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <line x1="116" y1="24" x2="124" y2="24" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <line x1="116" y1="30" x2="124" y2="34" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>''')

# Test - checkmark in a circle (test passing)
icons['clawd_test'] = svg('Run Tests', f'''  <circle cx="104" cy="22" r="18" fill="none" stroke="{GREEN}" stroke-width="3"/>
  <polyline points="94,22 100,28 114,14" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>''')

# Deploy - rocket
icons['clawd_deploy'] = svg('Deploy', f'''  <!-- rocket body -->
  <path d="M106,4 L114,20 L110,20 L110,36 L102,36 L102,20 L98,20 Z" fill="{RED}"/>
  <!-- window -->
  <circle cx="106" cy="18" r="3" fill="{WHITE}" opacity="0.7"/>
  <!-- fins -->
  <path d="M102,28 L96,36 L102,34 Z" fill="{BLUE}"/>
  <path d="M110,28 L116,36 L110,34 Z" fill="{BLUE}"/>
  <!-- flame -->
  <path d="M103,36 L106,44 L109,36" fill="{YELLOW}"/>
  <path d="M104,36 L106,40 L108,36" fill="{RED}" opacity="0.7"/>''')

# Install - package box with arrow down
icons['clawd_install'] = svg('Install', f'''  <!-- box -->
  <rect x="88" y="18" width="32" height="24" rx="2" fill="{BLUE}"/>
  <rect x="88" y="18" width="32" height="8" fill="{BLUE}" opacity="0.7"/>
  <line x1="104" y1="18" x2="104" y2="42" stroke="{WHITE}" stroke-width="2" opacity="0.3"/>
  <line x1="88" y1="26" x2="120" y2="26" stroke="{WHITE}" stroke-width="2" opacity="0.3"/>
  <!-- arrow down into box -->
  <line x1="104" y1="2" x2="104" y2="16" stroke="{GREEN}" stroke-width="3" stroke-linecap="round"/>
  <polyline points="98,10 104,16 110,10" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>''')

# Review - eye icon (code review)
icons['clawd_review'] = svg('Code Review', f'''  <!-- eye shape -->
  <path d="M82,22 Q106,2 126,22 Q106,42 82,22 Z" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <circle cx="104" cy="22" r="8" fill="{BLUE}"/>
  <circle cx="104" cy="22" r="4" fill="{DARK}"/>
  <circle cx="106" cy="20" r="2" fill="{WHITE}" opacity="0.6"/>''')

# === NEW ICONS: More States ===

# Success - celebration with confetti
icons['clawd_success'] = svg('Success', f'''  <!-- big checkmark above head -->
  <polyline points="40,16 50,28 72,4" fill="none" stroke="{GREEN}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- confetti -->
  <rect x="20" y="6" width="4" height="4" fill="{YELLOW}" transform="rotate(20,22,8)"/>
  <rect x="84" y="10" width="4" height="4" fill="{BLUE}" transform="rotate(-15,86,12)"/>
  <rect x="96" y="2" width="3" height="6" fill="{RED}" transform="rotate(30,97,5)"/>
  <rect x="110" y="12" width="4" height="3" fill="{GREEN}" transform="rotate(-25,112,13)"/>
  <rect x="60" y="2" width="3" height="5" fill="{MASCOT}" transform="rotate(10,61,4)"/>''')

# Confused - spiral + question marks
icons['clawd_confused'] = svg('Confused', f'''  <!-- spiral above head -->
  <path d="M52,24 Q52,8 64,8 Q76,8 76,18 Q76,26 66,26 Q58,26 60,20" fill="none" stroke="{YELLOW}" stroke-width="3" stroke-linecap="round"/>
  <!-- small ? -->
  <text x="84" y="16" font-family="monospace" font-size="16" fill="{YELLOW}" opacity="0.6">?</text>
  <text x="96" y="10" font-family="monospace" font-size="12" fill="{YELLOW}" opacity="0.4">?</text>''')

# Eureka - lightbulb moment
icons['clawd_eureka'] = svg('Eureka', f'''  <!-- lightbulb above head -->
  <circle cx="52" cy="14" r="12" fill="{YELLOW}" opacity="0.9"/>
  <rect x="48" y="26" width="8" height="4" rx="1" fill="{YELLOW}" opacity="0.7"/>
  <rect x="49" y="30" width="6" height="3" rx="1" fill="{YELLOW}" opacity="0.5"/>
  <!-- filament -->
  <path d="M50,14 Q52,8 54,14" fill="none" stroke="{DARK}" stroke-width="1.5" opacity="0.5"/>
  <!-- rays -->
  <g stroke="{YELLOW}" stroke-width="2" stroke-linecap="round" opacity="0.6">
    <line x1="52" y1="-2" x2="52" y2="0"/>
    <line x1="36" y1="8" x2="38" y2="10"/>
    <line x1="68" y1="8" x2="66" y2="10"/>
    <line x1="34" y1="20" x2="38" y2="18"/>
    <line x1="68" y1="20" x2="66" y2="18"/>
  </g>''')

# Focus - tunnel vision lines
icons['clawd_focus'] = svg('Focus', f'''  <!-- focus lines converging toward mascot -->
  <g stroke="{BLUE}" stroke-width="2" opacity="0.4" stroke-linecap="round">
    <line x1="0" y1="0" x2="24" y2="44"/>
    <line x1="128" y1="0" x2="88" y2="44"/>
    <line x1="0" y1="44" x2="16" y2="56"/>
    <line x1="128" y1="44" x2="100" y2="56"/>
    <line x1="0" y1="100" x2="20" y2="96"/>
    <line x1="128" y1="100" x2="100" y2="96"/>
  </g>
  <!-- intense eye glow -->
  <circle cx="31" cy="62" r="4" fill="{BLUE}" opacity="0.3"/>
  <circle cx="73" cy="62" r="4" fill="{BLUE}" opacity="0.3"/>''')

# === NEW ICONS: More Life ===

# Meditate - peaceful pose with aura
icons['clawd_meditate'] = svg('Meditating', f'''  <!-- aura circles -->
  <circle cx="52" cy="72" r="46" fill="none" stroke="{GREEN}" stroke-width="1.5" opacity="0.15"/>
  <circle cx="52" cy="72" r="38" fill="none" stroke="{GREEN}" stroke-width="1.5" opacity="0.25"/>
  <circle cx="52" cy="72" r="30" fill="none" stroke="{GREEN}" stroke-width="1.5" opacity="0.35"/>
  <!-- "om" sparkles -->
  <circle cx="20" cy="36" r="2" fill="{GREEN}" opacity="0.4"/>
  <circle cx="84" cy="40" r="2" fill="{GREEN}" opacity="0.4"/>
  <circle cx="52" cy="28" r="2" fill="{GREEN}" opacity="0.4"/>''')

# Rain - umbrella
icons['clawd_rain'] = svg('Rainy Day', f'''  <!-- umbrella -->
  <path d="M28,40 Q52,10 88,40" fill="{BLUE}" opacity="0.8"/>
  <line x1="52" y1="20" x2="52" y2="44" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
  <!-- rain drops -->
  <g fill="{BLUE}" opacity="0.4">
    <rect x="8" y="8" width="2" height="8" rx="1"/>
    <rect x="24" y="2" width="2" height="8" rx="1"/>
    <rect x="40" y="6" width="2" height="8" rx="1"/>
    <rect x="68" y="4" width="2" height="8" rx="1"/>
    <rect x="96" y="8" width="2" height="8" rx="1"/>
    <rect x="112" y="2" width="2" height="8" rx="1"/>
    <rect x="80" y="10" width="2" height="8" rx="1"/>
    <rect x="16" y="16" width="2" height="6" rx="1"/>
    <rect x="108" y="16" width="2" height="6" rx="1"/>
  </g>''')

# Love - hearts floating
icons['clawd_love'] = svg('Love', f'''  <g fill="{RED}">
    <!-- big heart -->
    <path d="M52,20 C52,12 40,8 40,18 C40,26 52,34 52,34 C52,34 64,26 64,18 C64,8 52,12 52,20 Z"/>
    <!-- small hearts -->
    <path d="M92,8 C92,4 86,2 86,6 C86,10 92,14 92,14 C92,14 98,10 98,6 C98,2 92,4 92,8 Z" opacity="0.6"/>
    <path d="M108,18 C108,15 104,14 104,16 C104,19 108,22 108,22 C108,22 112,19 112,16 C112,14 108,15 108,18 Z" opacity="0.4"/>
  </g>''')

# Workout - lifting dumbbell
icons['clawd_workout'] = svg('Working Out', f'''  <!-- dumbbell held above head -->
  <g fill="{DARK}">
    <!-- bar -->
    <rect x="20" y="34" width="72" height="4" rx="2"/>
    <!-- left weights -->
    <rect x="16" y="28" width="12" height="16" rx="2"/>
    <rect x="12" y="30" width="8" height="12" rx="1"/>
    <!-- right weights -->
    <rect x="84" y="28" width="12" height="16" rx="2"/>
    <rect x="92" y="30" width="8" height="12" rx="1"/>
  </g>
  <!-- effort lines -->
  <g stroke="{YELLOW}" stroke-width="2" stroke-linecap="round" opacity="0.5">
    <line x1="10" y1="26" x2="6" y2="20"/>
    <line x1="102" y1="26" x2="106" y2="20"/>
  </g>''')

# Cook - chef hat + pan
icons['clawd_cook'] = svg('Cooking', f'''  <!-- chef hat on head -->
  <rect x="24" y="34" width="56" height="10" fill="{WHITE}"/>
  <ellipse cx="52" cy="28" rx="24" ry="12" fill="{WHITE}"/>
  <!-- frying pan in right hand -->
  <circle cx="116" cy="72" r="12" fill="{DARK}" opacity="0.7"/>
  <circle cx="116" cy="72" r="10" fill="#666"/>
  <line x1="104" y1="72" x2="94" y2="72" stroke="{DARK}" stroke-width="3" stroke-linecap="round"/>
  <!-- steam from pan -->
  <g fill="none" stroke="{WHITE}" stroke-width="1.5" opacity="0.4">
    <path d="M112,58 Q114,54 112,50"/>
    <path d="M118,56 Q120,52 118,48"/>
  </g>''')

# Travel - suitcase
icons['clawd_travel'] = svg('Traveling', f'''  <!-- suitcase near right hand -->
  <rect x="98" y="62" width="24" height="30" rx="3" fill="{BLUE}"/>
  <rect x="98" y="62" width="24" height="8" rx="3" fill="{BLUE}" opacity="0.7"/>
  <!-- suitcase details -->
  <line x1="98" y1="76" x2="122" y2="76" stroke="{WHITE}" stroke-width="1.5" opacity="0.3"/>
  <rect x="106" y="58" width="8" height="6" rx="2" fill="none" stroke="{BLUE}" stroke-width="2"/>
  <!-- wheels -->
  <circle cx="104" cy="94" r="2" fill="{DARK}"/>
  <circle cx="116" cy="94" r="2" fill="{DARK}"/>''')

# Photo - camera
icons['clawd_photo'] = svg('Taking Photo', f'''  <!-- camera in right hand -->
  <rect x="94" y="60" width="30" height="22" rx="3" fill="{DARK}"/>
  <circle cx="109" cy="72" r="7" fill="none" stroke="{BLUE}" stroke-width="2.5"/>
  <circle cx="109" cy="72" r="3" fill="{BLUE}" opacity="0.4"/>
  <rect x="100" y="60" width="10" height="4" rx="1" fill="{DARK}"/>
  <!-- flash -->
  <rect x="118" y="62" width="4" height="4" rx="1" fill="{YELLOW}" opacity="0.8"/>
  <!-- flash burst -->
  <g stroke="{YELLOW}" stroke-width="1.5" stroke-linecap="round" opacity="0.4">
    <line x1="124" y1="58" x2="126" y2="54"/>
    <line x1="126" y1="64" x2="128" y2="64"/>
    <line x1="124" y1="70" x2="126" y2="74"/>
  </g>''')

# Dance - motion + musical notes
icons['clawd_dance'] = svg('Dancing', f'''  <!-- extended arm up-right (waving while dancing) -->
  <g fill="{MASCOT}">
    <rect x="100" y="50" width="10" height="10"/>
    <rect x="106" y="40" width="10" height="14"/>
    <rect x="112" y="34" width="8" height="10"/>
  </g>
  <!-- musical notes around -->
  <text x="16" y="20" font-family="serif" font-size="16" fill="{GREEN}" opacity="0.7">&#9835;</text>
  <text x="100" y="12" font-family="serif" font-size="14" fill="{BLUE}" opacity="0.6">&#9834;</text>
  <text x="116" y="24" font-family="serif" font-size="12" fill="{YELLOW}" opacity="0.5">&#9835;</text>
  <!-- motion swoosh -->
  <path d="M4,88 Q0,80 4,72" fill="none" stroke="{GREEN}" stroke-width="2" stroke-linecap="round" opacity="0.4"/>''')

# Pet - small cat/dog next to mascot
icons['clawd_pet'] = svg('With Pet', f'''  <!-- small pixel cat next to left side -->
  <g fill="#888">
    <!-- cat body -->
    <rect x="0" y="88" width="14" height="10"/>
    <!-- cat head -->
    <rect x="-2" y="82" width="10" height="8"/>
    <!-- ears -->
    <rect x="-2" y="78" width="4" height="4"/>
    <rect x="4" y="78" width="4" height="4"/>
    <!-- tail -->
    <rect x="12" y="82" width="4" height="4"/>
    <rect x="16" y="78" width="4" height="4"/>
    <!-- eye -->
    <rect x="1" y="84" width="2" height="2" fill="{GREEN}"/>
  </g>''')

# Birthday - cake with candle
icons['clawd_birthday'] = svg('Birthday', f'''  <!-- cake on right side -->
  <rect x="94" y="72" width="28" height="16" rx="2" fill="#E8A0C0"/>
  <rect x="94" y="72" width="28" height="6" rx="2" fill="#F0C0D8"/>
  <rect x="94" y="84" width="28" height="4" fill="#D080A0"/>
  <!-- frosting drips -->
  <rect x="98" y="70" width="4" height="4" rx="2" fill="{WHITE}"/>
  <rect x="110" y="70" width="4" height="4" rx="2" fill="{WHITE}"/>
  <!-- candle -->
  <rect x="106" y="60" width="4" height="12" fill="{YELLOW}"/>
  <!-- flame -->
  <ellipse cx="108" cy="58" rx="3" ry="4" fill="{YELLOW}"/>
  <ellipse cx="108" cy="58" rx="2" ry="3" fill="{RED}" opacity="0.6"/>''')

# === NEW: More Dev Tool Icons ===

# Curl / HTTP request
icons['clawd_curl'] = svg('HTTP Request', f'''  <!-- request arrow going right -->
  <line x1="82" y1="14" x2="114" y2="14" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>
  <polyline points="106,8 114,14 106,20" fill="none" stroke="{BLUE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- response arrow coming back -->
  <line x1="114" y1="30" x2="82" y2="30" stroke="{GREEN}" stroke-width="3" stroke-linecap="round" stroke-dasharray="4,3"/>
  <polyline points="90,24 82,30 90,36" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- status badge -->
  <rect x="96" y="36" width="26" height="10" rx="2" fill="{GREEN}"/>
  <text x="109" y="44" text-anchor="middle" font-family="monospace" font-size="8" fill="{WHITE}" font-weight="bold">200</text>''')

# Docker / Container
icons['clawd_docker'] = svg('Docker', f'''  <!-- container box -->
  <rect x="84" y="14" width="36" height="28" rx="2" fill="{BLUE}"/>
  <!-- container grid lines -->
  <line x1="96" y1="14" x2="96" y2="42" stroke="{WHITE}" stroke-width="1" opacity="0.3"/>
  <line x1="108" y1="14" x2="108" y2="42" stroke="{WHITE}" stroke-width="1" opacity="0.3"/>
  <line x1="84" y1="24" x2="120" y2="24" stroke="{WHITE}" stroke-width="1" opacity="0.3"/>
  <line x1="84" y1="34" x2="120" y2="34" stroke="{WHITE}" stroke-width="1" opacity="0.3"/>
  <!-- whale tail (docker-ish) -->
  <rect x="88" y="8" width="6" height="6" rx="1" fill="{BLUE}" opacity="0.6"/>
  <rect x="96" y="8" width="6" height="6" rx="1" fill="{BLUE}" opacity="0.6"/>
  <rect x="104" y="8" width="6" height="6" rx="1" fill="{BLUE}" opacity="0.6"/>
  <rect x="92" y="2" width="6" height="6" rx="1" fill="{BLUE}" opacity="0.4"/>
  <rect x="100" y="2" width="6" height="6" rx="1" fill="{BLUE}" opacity="0.4"/>''')

# SSH - remote terminal connection
icons['clawd_ssh'] = svg('SSH', f'''  <!-- terminal window -->
  <rect x="82" y="4" width="42" height="34" rx="3" fill="{DARK}"/>
  <rect x="82" y="4" width="42" height="8" rx="3" fill="#555"/>
  <!-- dots on title bar -->
  <circle cx="88" cy="8" r="2" fill="{RED}" opacity="0.7"/>
  <circle cx="94" cy="8" r="2" fill="{YELLOW}" opacity="0.7"/>
  <circle cx="100" cy="8" r="2" fill="{GREEN}" opacity="0.7"/>
  <!-- prompt text -->
  <rect x="86" y="16" width="20" height="2" fill="{GREEN}" opacity="0.8"/>
  <rect x="86" y="22" width="30" height="2" fill="{WHITE}" opacity="0.5"/>
  <rect x="86" y="28" width="14" height="2" fill="{GREEN}" opacity="0.8"/>
  <!-- connection line + lock -->
  <line x1="102" y1="38" x2="102" y2="48" stroke="{BLUE}" stroke-width="2" stroke-dasharray="3,2"/>
  <rect x="96" y="46" width="12" height="10" rx="2" fill="{YELLOW}"/>
  <rect x="98" y="42" width="8" height="6" rx="4" fill="none" stroke="{YELLOW}" stroke-width="2"/>''')

# Database operations
icons['clawd_db'] = svg('Database', f'''  <!-- database cylinder -->
  <ellipse cx="104" cy="10" rx="18" ry="8" fill="{BLUE}"/>
  <rect x="86" y="10" width="36" height="28" fill="{BLUE}"/>
  <ellipse cx="104" cy="38" rx="18" ry="8" fill="{BLUE}" opacity="0.8"/>
  <!-- middle ring -->
  <ellipse cx="104" cy="24" rx="18" ry="6" fill="none" stroke="{WHITE}" stroke-width="1.5" opacity="0.3"/>
  <!-- top highlight -->
  <ellipse cx="104" cy="10" rx="12" ry="4" fill="{WHITE}" opacity="0.15"/>''')

# API endpoint
icons['clawd_api'] = svg('API', f'''  <!-- API badge -->
  <rect x="82" y="6" width="42" height="18" rx="4" fill="{BLUE}"/>
  <text x="103" y="19" text-anchor="middle" font-family="monospace" font-size="12" fill="{WHITE}" font-weight="bold">API</text>
  <!-- endpoint dots connected -->
  <circle cx="88" cy="36" r="4" fill="{GREEN}"/>
  <circle cx="104" cy="44" r="4" fill="{GREEN}"/>
  <circle cx="120" cy="36" r="4" fill="{GREEN}"/>
  <line x1="88" y1="36" x2="104" y2="44" stroke="{GREEN}" stroke-width="2"/>
  <line x1="104" y1="44" x2="120" y2="36" stroke="{GREEN}" stroke-width="2"/>
  <line x1="88" y1="36" x2="120" y2="36" stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="3,2" opacity="0.4"/>''')

# Lint / Format
icons['clawd_lint'] = svg('Lint / Format', f'''  <!-- sparkle/wand for "cleaning up" -->
  <line x1="112" y1="4" x2="92" y2="40" stroke="{YELLOW}" stroke-width="3" stroke-linecap="round"/>
  <!-- star tip -->
  <g fill="{YELLOW}">
    <polygon points="112,4 114,0 116,4 120,4 116,7 118,12 112,8 106,12 108,7 104,4"/>
  </g>
  <!-- sparkles -->
  <g fill="{YELLOW}" opacity="0.5">
    <rect x="84" y="14" width="3" height="3" rx="1"/>
    <rect x="96" y="24" width="3" height="3" rx="1"/>
    <rect x="86" y="34" width="3" height="3" rx="1"/>
  </g>''')

# Build / Compile
icons['clawd_build'] = svg('Build', f'''  <!-- hammer -->
  <rect x="90" y="6" width="24" height="12" rx="2" fill="#888"/>
  <rect x="90" y="6" width="12" height="12" rx="2" fill="#999"/>
  <rect x="100" y="18" width="4" height="24" rx="1" fill="#A0764A"/>
  <!-- sparks -->
  <g fill="{YELLOW}" opacity="0.6">
    <rect x="84" y="16" width="3" height="3" rx="1"/>
    <rect x="80" y="10" width="2" height="2" rx="1"/>
    <rect x="86" y="22" width="2" height="2" rx="1"/>
  </g>''')

# Git Merge
icons['clawd_merge'] = svg('Git Merge', f'''  <!-- merge diagram -->
  <circle cx="90" cy="8" r="5" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <circle cx="118" cy="8" r="5" fill="none" stroke="{GREEN}" stroke-width="3"/>
  <circle cx="104" cy="42" r="5" fill="none" stroke="{YELLOW}" stroke-width="3"/>
  <line x1="90" y1="13" x2="104" y2="37" stroke="{BLUE}" stroke-width="2.5"/>
  <line x1="118" y1="13" x2="104" y2="37" stroke="{GREEN}" stroke-width="2.5"/>''')

# Pull Request
icons['clawd_pr'] = svg('Pull Request', f'''  <!-- PR icon -->
  <circle cx="90" cy="10" r="5" fill="none" stroke="{GREEN}" stroke-width="3"/>
  <circle cx="118" cy="40" r="5" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <line x1="90" y1="15" x2="90" y2="36" stroke="{GREEN}" stroke-width="2.5"/>
  <circle cx="90" cy="40" r="4" fill="{GREEN}"/>
  <!-- arrow from left to right -->
  <path d="M94,30 Q104,30 110,36" fill="none" stroke="{BLUE}" stroke-width="2.5" stroke-linecap="round"/>
  <polyline points="106,32 112,36 108,40" fill="none" stroke="{BLUE}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>''')

# Git Commit
icons['clawd_commit'] = svg('Git Commit', f'''  <!-- commit node -->
  <line x1="104" y1="2" x2="104" y2="16" stroke="{BLUE}" stroke-width="3"/>
  <circle cx="104" cy="24" r="8" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <circle cx="104" cy="24" r="3" fill="{BLUE}"/>
  <line x1="104" y1="32" x2="104" y2="46" stroke="{BLUE}" stroke-width="3"/>
  <!-- message hint -->
  <rect x="114" y="18" width="14" height="12" rx="2" fill="{GREEN}" opacity="0.6"/>
  <rect x="116" y="22" width="10" height="2" fill="{WHITE}" opacity="0.5"/>
  <rect x="116" y="26" width="6" height="2" fill="{WHITE}" opacity="0.5"/>''')

# Diff - side by side comparison
icons['clawd_diff'] = svg('Diff', f'''  <!-- left file -->
  <rect x="80" y="4" width="20" height="40" rx="2" fill="{RED}" opacity="0.7"/>
  <rect x="84" y="10" width="12" height="2" fill="{WHITE}" opacity="0.5"/>
  <rect x="84" y="16" width="10" height="2" fill="{WHITE}" opacity="0.5"/>
  <rect x="84" y="22" width="12" height="2" fill="{WHITE}" opacity="0.3"/>
  <rect x="84" y="28" width="8" height="2" fill="{WHITE}" opacity="0.5"/>
  <!-- right file -->
  <rect x="104" y="4" width="20" height="40" rx="2" fill="{GREEN}" opacity="0.7"/>
  <rect x="108" y="10" width="12" height="2" fill="{WHITE}" opacity="0.5"/>
  <rect x="108" y="16" width="10" height="2" fill="{WHITE}" opacity="0.5"/>
  <rect x="108" y="22" width="14" height="2" fill="{WHITE}" opacity="0.7"/>
  <rect x="108" y="28" width="8" height="2" fill="{WHITE}" opacity="0.5"/>
  <!-- arrows between -->
  <text x="100" y="24" text-anchor="middle" font-family="monospace" font-size="12" fill="{YELLOW}">&#x2194;</text>''')

# Log / Monitoring
icons['clawd_log'] = svg('Logs', f'''  <!-- scrolling log lines -->
  <rect x="82" y="4" width="42" height="44" rx="3" fill="{DARK}"/>
  <rect x="86" y="10" width="6" height="2" fill="{BLUE}" opacity="0.6"/>
  <rect x="94" y="10" width="24" height="2" fill="{WHITE}" opacity="0.3"/>
  <rect x="86" y="16" width="6" height="2" fill="{GREEN}" opacity="0.6"/>
  <rect x="94" y="16" width="20" height="2" fill="{WHITE}" opacity="0.3"/>
  <rect x="86" y="22" width="6" height="2" fill="{YELLOW}" opacity="0.6"/>
  <rect x="94" y="22" width="26" height="2" fill="{WHITE}" opacity="0.3"/>
  <rect x="86" y="28" width="6" height="2" fill="{RED}" opacity="0.6"/>
  <rect x="94" y="28" width="18" height="2" fill="{WHITE}" opacity="0.5"/>
  <rect x="86" y="34" width="6" height="2" fill="{BLUE}" opacity="0.6"/>
  <rect x="94" y="34" width="22" height="2" fill="{WHITE}" opacity="0.3"/>
  <rect x="86" y="40" width="6" height="2" fill="{GREEN}" opacity="0.6"/>
  <rect x="94" y="40" width="16" height="2" fill="{WHITE}" opacity="0.3"/>''')

# CI/CD Pipeline
icons['clawd_ci'] = svg('CI/CD', f'''  <!-- pipeline stages -->
  <circle cx="86" cy="22" r="6" fill="{GREEN}"/>
  <polyline points="86,22 84,20 82,22" fill="none" stroke="{WHITE}" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="92" y1="22" x2="98" y2="22" stroke="{BLUE}" stroke-width="2"/>
  <circle cx="104" cy="22" r="6" fill="{BLUE}"/>
  <rect x="101" y="19" width="6" height="6" rx="1" fill="none" stroke="{WHITE}" stroke-width="1.5"/>
  <line x1="110" y1="22" x2="116" y2="22" stroke="{BLUE}" stroke-width="2"/>
  <circle cx="122" cy="22" r="6" fill="{YELLOW}"/>
  <!-- loading spinner in last stage -->
  <path d="M122,16 A6,6 0 0,1 128,22" fill="none" stroke="{WHITE}" stroke-width="1.5" stroke-linecap="round"/>
  <!-- arrows -->
  <polyline points="96,20 98,22 96,24" fill="none" stroke="{BLUE}" stroke-width="1.5" stroke-linecap="round"/>
  <polyline points="114,20 116,22 114,24" fill="none" stroke="{BLUE}" stroke-width="1.5" stroke-linecap="round"/>''')

# Config / Settings
icons['clawd_config'] = svg('Config', f'''  <!-- gear -->
  <g transform="translate(104,22)">
    <circle cx="0" cy="0" r="7" fill="none" stroke="{BLUE}" stroke-width="3"/>
    <circle cx="0" cy="0" r="3" fill="{BLUE}"/>
    <!-- gear teeth -->
    <g fill="{BLUE}">
      <rect x="-2" y="-14" width="4" height="6" rx="1"/>
      <rect x="-2" y="8" width="4" height="6" rx="1"/>
      <rect x="-14" y="-2" width="6" height="4" rx="1"/>
      <rect x="8" y="-2" width="6" height="4" rx="1"/>
      <rect x="6" y="-10" width="5" height="4" rx="1" transform="rotate(45,8,-8)"/>
      <rect x="-11" y="6" width="5" height="4" rx="1" transform="rotate(45,-8,8)"/>
      <rect x="-11" y="-10" width="5" height="4" rx="1" transform="rotate(-45,-8,-8)"/>
      <rect x="6" y="6" width="5" height="4" rx="1" transform="rotate(-45,8,8)"/>
    </g>
  </g>''')

# Env / Environment variables
icons['clawd_env'] = svg('Environment', f'''  <!-- .env file -->
  <rect x="84" y="4" width="38" height="42" rx="3" fill="{DARK}"/>
  <text x="90" y="16" font-family="monospace" font-size="8" fill="{GREEN}" opacity="0.9">.env</text>
  <rect x="88" y="20" width="14" height="2" fill="{YELLOW}" opacity="0.7"/>
  <rect x="104" y="20" width="10" height="2" fill="{WHITE}" opacity="0.4"/>
  <rect x="88" y="26" width="10" height="2" fill="{YELLOW}" opacity="0.7"/>
  <rect x="100" y="26" width="16" height="2" fill="{WHITE}" opacity="0.4"/>
  <rect x="88" y="32" width="16" height="2" fill="{YELLOW}" opacity="0.7"/>
  <rect x="106" y="32" width="8" height="2" fill="{WHITE}" opacity="0.4"/>
  <rect x="88" y="38" width="8" height="2" fill="{YELLOW}" opacity="0.7"/>
  <rect x="98" y="38" width="12" height="2" fill="{WHITE}" opacity="0.4"/>''')

# Output directory
OUT = 'icons'

for name, content in icons.items():
    path = os.path.join(OUT, f'{name}.svg')
    with open(path, 'w') as f:
        f.write(content)
    print(f'Created {path}')

# Generate preview HTML
preview = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Clawd Icon Set Preview</title>
<style>
  body {
    background: #1a1a2e;
    color: #eee;
    font-family: 'SF Mono', 'Fira Code', monospace;
    padding: 40px;
    margin: 0;
  }
  h1 { color: #D97757; text-align: center; margin-bottom: 8px; }
  h2 { color: #888; margin-top: 40px; margin-bottom: 16px; border-bottom: 1px solid #333; padding-bottom: 8px; }
  .subtitle { text-align: center; color: #666; margin-bottom: 40px; }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 20px;
  }
  .icon-card {
    background: #16213e;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    transition: transform 0.2s, box-shadow 0.2s;
    border: 1px solid #333;
  }
  .icon-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(217,119,87,0.2);
    border-color: #D97757;
  }
  .icon-card img {
    width: 96px;
    height: 96px;
    margin-bottom: 12px;
  }
  .icon-card .name {
    font-size: 12px;
    color: #aaa;
    word-break: break-all;
  }
  .icon-card .label {
    font-size: 14px;
    color: #D97757;
    margin-bottom: 4px;
  }
</style>
</head>
<body>
<h1>Clawd Icon Set</h1>
<p class="subtitle">Claude Code Mascot Action Icons</p>
'''

sections = {
    'Tools': [
        ('clawd_read', 'Read File'),
        ('clawd_edit', 'Edit File'),
        ('clawd_write', 'Write File'),
        ('clawd_bash', 'Bash Terminal'),
        ('clawd_glob', 'Glob Search'),
        ('clawd_grep', 'Grep Search'),
        ('clawd_lsp', 'Code Intelligence'),
        ('clawd_webfetch', 'Web Fetch'),
        ('clawd_websearch', 'Web Search'),
        ('clawd_notebook', 'Notebook Edit'),
    ],
    'Dev Actions': [
        ('clawd_git', 'Git'),
        ('clawd_commit', 'Commit'),
        ('clawd_merge', 'Merge'),
        ('clawd_pr', 'Pull Request'),
        ('clawd_diff', 'Diff'),
        ('clawd_debug', 'Debug'),
        ('clawd_test', 'Run Tests'),
        ('clawd_build', 'Build'),
        ('clawd_deploy', 'Deploy'),
        ('clawd_install', 'Install'),
        ('clawd_lint', 'Lint/Format'),
        ('clawd_review', 'Code Review'),
        ('clawd_curl', 'HTTP Request'),
        ('clawd_docker', 'Docker'),
        ('clawd_ssh', 'SSH'),
        ('clawd_db', 'Database'),
        ('clawd_api', 'API'),
        ('clawd_log', 'Logs'),
        ('clawd_ci', 'CI/CD'),
        ('clawd_config', 'Config'),
        ('clawd_env', 'Env Vars'),
    ],
    'Subagent & States': [
        ('clawd_agent', 'Spawn Agent'),
        ('clawd_explore', 'Explore'),
        ('clawd_plan', 'Plan'),
        ('clawd_think', 'Thinking'),
        ('clawd_answer', 'Answering'),
        ('clawd_ask', 'Asking'),
        ('clawd_wait', 'Waiting'),
        ('clawd_error', 'Error'),
        ('clawd_success', 'Success'),
        ('clawd_confused', 'Confused'),
        ('clawd_eureka', 'Eureka'),
        ('clawd_focus', 'Focus'),
    ],
    'Life': [
        ('clawd_rest', 'Resting'),
        ('clawd_run', 'Running'),
        ('clawd_sleep', 'Sleeping'),
        ('clawd_drink', 'Drinking'),
        ('clawd_eat', 'Eating'),
        ('clawd_coffee', 'Coffee'),
        ('clawd_happy', 'Happy'),
        ('clawd_sad', 'Sad'),
        ('clawd_music', 'Music'),
        ('clawd_game', 'Gaming'),
        ('clawd_read_book', 'Reading'),
        ('clawd_wave', 'Waving'),
        ('clawd_meditate', 'Meditating'),
        ('clawd_rain', 'Rainy Day'),
        ('clawd_love', 'Love'),
        ('clawd_workout', 'Working Out'),
        ('clawd_cook', 'Cooking'),
        ('clawd_travel', 'Traveling'),
        ('clawd_photo', 'Photo'),
        ('clawd_dance', 'Dancing'),
        ('clawd_pet', 'With Pet'),
        ('clawd_birthday', 'Birthday'),
    ],
}

for section, items in sections.items():
    preview += f'<h2>{section}</h2>\n<div class="grid">\n'
    for fname, label in items:
        preview += f'''  <div class="icon-card">
    <img src="{fname}.svg" alt="{label}">
    <div class="label">{label}</div>
    <div class="name">{fname}.svg</div>
  </div>\n'''
    preview += '</div>\n'

preview += '</body>\n</html>\n'

with open(os.path.join(OUT, 'preview.html'), 'w') as f:
    f.write(preview)
print(f'Created {os.path.join(OUT, "preview.html")}')
print(f'\nTotal: {len(icons)} icons generated')
