# Neon Coast Cover Studio

[![make.fun · gta6-cover-art-01](https://make.fun/badge/gta6-cover-art-01.svg)](https://make.fun/bounty/gta6-cover-art-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-cover-art-01)
[![rank](https://make.fun/badge/gta6-cover-art-01/Reki120/gta6-cover-art-01/rank.svg)](https://make.fun/bounty/gta6-cover-art-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-cover-art-01)
[![reward](https://make.fun/badge/gta6-cover-art-01/Reki120/gta6-cover-art-01/reward.svg)](https://make.fun/bounty/gta6-cover-art-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-cover-art-01)

Turn your photos into original GTA-style coastal crime-poster cover art. Compose five panel layouts, reframe each photo, dial in five colour treatments, and add your own headline, script subtitle, badge and heat meter. Export a square, portrait or landscape PNG. All editing happens locally, with no uploads, accounts, dependencies or build step.

## Run it

```sh
node serve.ts
```

Then open http://localhost:8080. Two bundled sample photos make the studio ready immediately. Select a panel, choose a tray photo, then drag and zoom to crop. Switch on Span for a continuous image across the layout. The three size buttons update the composition and download a full-resolution PNG.

Screenshot scenes: `?shot=editor` shows the studio; `?shot=cover&layout=classic&grade=sunset&size=1080x1350` shows only the artwork. Cover scenes also accept `title`, `subtitle` and `caption`. Layout IDs: classic, hero, triple, quad, full. Grade IDs: sunset, neon, gold, noir, clean.

Anton and Pacifico downloads were attempted from Google Fonts, but the network proxy was unavailable. This version uses heavy system display lettering and an italic script/cursive fallback. No official game fonts, marks or artwork are included. Sample images are the starter’s freely usable generated photos.

To package: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`.

Entered on [make.fun](https://make.fun/?ref=rwf799wr&utm_source=github&utm_medium=readme&utm_campaign=gta6-cover-art-01)
