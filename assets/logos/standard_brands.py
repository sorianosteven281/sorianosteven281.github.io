import os

svgs = {
    "rockwell.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 50" width="220" height="50">
  <g transform="translate(10, 8)">
    <polygon points="12,17 18,5 30,5 36,17 30,29 18,29" fill="#D32F2F"/>
    <polygon points="18,17 20,10 28,10 30,17 28,24 20,24" fill="#FFFFFF"/>
    <polygon points="22,17 23,13 25,13 26,17 25,21 23,21" fill="#D32F2F"/>
    <text x="44" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="17" fill="#0F172A" letter-spacing="-0.3">Rockwell</text>
    <text x="44" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="10" fill="#D32F2F" letter-spacing="1.2">AUTOMATION</text>
  </g>
</svg>''',

    "siemens.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 50" width="180" height="50">
  <g transform="translate(10, 10)">
    <text x="80" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif" font-weight="900" font-size="28" fill="#00646E" text-anchor="middle" letter-spacing="2">SIEMENS</text>
  </g>
</svg>''',

    "schneider.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50" width="200" height="50">
  <g transform="translate(10, 8)">
    <text x="90" y="17" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="18" fill="#3DCD58" text-anchor="middle" letter-spacing="0.5">Schneider</text>
    <text x="90" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="10" fill="#0F172A" text-anchor="middle" letter-spacing="2.5">ELECTRIC</text>
  </g>
</svg>''',

    "abb.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 50" width="140" height="50">
  <g transform="translate(10, 10)">
    <text x="60" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="34" fill="#FF000F" text-anchor="middle" font-style="italic" letter-spacing="2">ABB</text>
  </g>
</svg>''',

    "fluke.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 50" width="150" height="50">
  <g transform="translate(10, 10)">
    <rect x="5" y="2" width="120" height="28" rx="4" fill="#FFC20E"/>
    <text x="65" y="23" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="20" fill="#000000" text-anchor="middle" font-style="italic" letter-spacing="1">FLUKE</text>
  </g>
</svg>''',

    "phoenix.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50" width="200" height="50">
  <g transform="translate(8, 8)">
    <circle cx="16" cy="16" r="14" fill="#005A5B"/>
    <path d="M10,16 L14,10 L18,22 L22,16" stroke="#FFFFFF" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <text x="38" y="17" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="15" fill="#005A5B" letter-spacing="0.5">PHOENIX</text>
    <text x="38" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="#005A5B" letter-spacing="1">CONTACT</text>
  </g>
</svg>''',

    "etap.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 50" width="170" height="50">
  <g transform="translate(8, 8)">
    <text x="5" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="30" fill="#C8102E" letter-spacing="-1.5">etap</text>
    <text x="75" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="9" fill="#334155" letter-spacing="1">POWER</text>
    <text x="75" y="25" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="9" fill="#334155" letter-spacing="1">SYSTEMS</text>
  </g>
</svg>''',

    "digsilent.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 50" width="180" height="50">
  <g transform="translate(8, 8)">
    <text x="5" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="20" fill="#003366" letter-spacing="-0.3">DIgSILENT</text>
    <text x="5" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="9" fill="#0284C7" letter-spacing="1.5">PowerFactory</text>
  </g>
</svg>'''
}

for name, content in svgs.items():
    p = os.path.join('/data/data/com.termux/files/home/cb-soluciones-web/public/assets/logos/', name)
    with open(p, 'w') as f:
        f.write(content)
    print('Generated', name)
