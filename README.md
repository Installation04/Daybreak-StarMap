# Daybreak Star Map

A GPU-accelerated 3D star map of the Project Daybreak universe, laid over the real Milky Way: the Human Sphere and the Covenant Sphere, their slipspace routes and a route calculator, the Halo Array, and a field of 1,347,197 catalogue stars with the nebulae, clusters and Local Group galaxies around them. Built by Faber and Tacitus: Faber built the map, Tacitus made the Project Daybreak charts and galaxy map it follows.

Halo is a trademark of Microsoft Corporation. This is a fan-made, non-commercial work created under Microsoft's [Game Content Usage Rules](https://www.xbox.com/en-US/developers/rules); it is not endorsed by or affiliated with Microsoft.

## Getting the map

**Windows app.** Download the installer from the [Releases](https://github.com/Installation04/Daybreak-StarMap/releases) page (`.exe` is the NSIS installer, `.msi` the Windows Installer package). Windows 10 or 11; the WebView2 runtime is fetched on first install if the machine does not have it. Nothing else is downloaded: the map runs entirely offline.

**In a browser.** Download this repository (the green Code button, Download ZIP), unzip it, and run

    python3 tools/serve.py

then open http://localhost:8080/. A browser will not load the map's binaries from a `file://` URL, so double-clicking `app/index.html` does not work; the little server is the smallest thing that does. Any static file server pointed at `app/` will do the same.

## Layout

    app/            the map: index.html, the star field (stars.wasm, stars2.wasm, starids.wasm, starids2.wasm,
                    gaia.wasm, gaia2.wasm: the Gaia DR3 shell out to 200 pc),
                    clouds.wasm, tex/, help/, fonts/
    src-tauri/      the desktop shell (Tauri 2)
    tools/          build_release.py (turns a published page into app/index.html), serve.py
    .github/        the release workflow: push a tag like v0.27.0 and the installers appear on a draft release

The page in `app/` is the whole program; the desktop shell only hosts it in the system webview and passes its outbound links to the default browser.

## Building the desktop app yourself

Install [Rust](https://www.rust-lang.org/tools/install) and Node, then

    npm install
    npm run dev      # runs the app
    npm run build    # writes installers to src-tauri/target/release/bundle/

## Sources and credits

Every source is credited in the app's About sheet (the ⓘ button) and listed in [CREDITS.md](CREDITS.md). In short: lore and placements from the [Project Daybreak Wiki](https://daybreak.miraheze.org/) (CC BY-SA 4.0) and the Daybreak charts by Tacitus; stars from [AT-HYG](https://codeberg.org/astronexus/athyg) v4.0 (CC BY-SA 4.0), the Gaia Catalogue of Nearby Stars, a Gaia DR3 shell out to 200 pc (ESA Gaia Archive) and SIMBAD, with 2MASS and CATWISE names; deep-sky objects from Harris (globular clusters), Green (supernova remnants), McConnachie (Local Group) and Wikipedia; constellation figures from Stellarium; planet textures from Solar System Scope (CC BY 4.0) and NASA 3D Resources (public domain); three.js (MIT); fonts under the SIL Open Font Licence.

## Licence

The map's own code (the page's scripts, the desktop shell, the tools) is released under the [MIT Licence](LICENSE). The Daybreak placement data embedded in the page (system positions, routes, regions, the Covenant feature names) and the star-field binaries derived from the catalogues are released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), matching the wiki and the catalogues they derive from; see [LICENSE-DATA.md](LICENSE-DATA.md). Third-party data and images keep their own terms, listed in CREDITS.md.

## Reporting an error

Distances and positions in fiction are often contradictory. If you have a source that beats the one the map used, the object's panel names what it used; open an issue with the object and the source.
