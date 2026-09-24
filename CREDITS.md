# Credits and sources

This file mirrors the app's About sheet (the ⓘ button). If the two differ, the About sheet in the shipped page is the one to fix.

## Creators

- **Faber**
- **Tacitus**

## Halo

Halo © Microsoft Corporation. The Daybreak Star Map was created under Microsoft's [Game Content Usage Rules](https://www.xbox.com/en-US/developers/rules) using assets from Halo, and it is not endorsed by or affiliated with Microsoft. Non-commercial.

## Lore

- **Project Daybreak Wiki**, https://daybreak.miraheze.org/, CC BY-SA 4.0. Where an object has a wiki article, its opening lines are quoted as the overview, attributed and linked in the panel.
- **Daybreak charts**: the Human Sphere chart (2565), the ONI Project LEVIATHAN Spinward strategic map (2576), the Siakar Expanse chart, the Covenant Sphere heatmap (1,000 ly grid), and the Daybreak galaxy map ("The Milky Way / Project LEVIATHAN", Tacitus, 2021) for the Halo Array. Where a chart and a wiki page disagree, the map follows the chart.

## Star catalogues

- **Augmented Tycho-HYG (AT-HYG) v4.0**, David Nash (astronexus), https://codeberg.org/astronexus/athyg, CC BY-SA 4.0. 354,212 of the 634,031 stars in the field, the named-star list and the HIP, HD, HR, Gliese, Bayer, Flamsteed, Tycho-2 and Gaia DR3 designations come from it. AT-HYG is itself compiled from Hipparcos and Tycho-2 (ESA), Gaia DR3, the Henry Draper catalogue, the Yale Bright Star Catalogue, the Gliese-Jahreiss catalogue and the IAU star names. The Hipparcos distance switch in Settings uses the HYG parallaxes carried in the same catalogue.
- **Gaia Catalogue of Nearby Stars (GCNS)**: Gaia Collaboration, Smart, R. L., et al. 2021, A&A, 649, A6, "Gaia Early Data Release 3: The Gaia Catalogue of Nearby Stars", via the CDS VizieR catalogue J/A+A/649/A6. The 279,819 faint stars and brown dwarfs within 100 pc that AT-HYG does not carry, with their Gaia EDR3, 2MASS and CATWISE names, come from it. The 863 brown dwarfs (767 typed by SIMBAD, 96 candidates by colour and absolute magnitude) are drawn and typed as such.
- **SIMBAD**: This research has made use of the SIMBAD database, operated at CDS, Strasbourg, France (Wenger, M., et al. 2000, A&AS, 143, 9). Every other identifier a star carries, its object type, and the adopted parallax that places each star within 100 pc (Gaia DR3, Gaia DR2, Hipparcos or Gliese-Jahreiss, whichever SIMBAD adopts) come from a SIMBAD extract taken on 23 September 2026.
- **2MASS**: Two Micron All Sky Survey, Skrutskie, M. F., et al. 2006, AJ, 131, 1163 (names as carried by GCNS).
- **CATWISE2020**: Marocco, F., et al. 2021, ApJS, 253, 8 (names as carried by GCNS).
- **Gaia**: This work has made use of data from the European Space Agency (ESA) mission Gaia (https://www.cosmos.esa.int/gaia), processed by the Gaia Data Processing and Analysis Consortium (DPAC, https://www.cosmos.esa.int/web/gaia/dpac/consortium). Funding for the DPAC has been provided by national institutions, in particular the institutions participating in the Gaia Multilateral Agreement.

## Deep-sky data

- **Globular clusters**: Harris, W. E. 1996, AJ, 112, 1487 (2010 edition), https://physics.mcmaster.ca/~harris/mwgc.dat
- **Supernova remnants**: Green, D. A. 2024, "A Catalogue of Galactic Supernova Remnants (2024 October version)", Cavendish Laboratory, Cambridge; Green, D. A. 2025, Journal of Astrophysics and Astronomy, 46, 14. Distances from the papers named in each remnant's panel.
- **Local Group galaxies**: McConnachie, A. W. 2012, AJ, 144, 4, "The Observed Properties of Dwarf Galaxies in and around the Local Group", with later discoveries from Wikipedia (CC BY-SA 4.0).
- **Nebulae, molecular clouds and open clusters**: positions and distances from Wikipedia (CC BY-SA 4.0) and the papers named in each object's panel, with Gaia distances where they exist.
- **Constellation figures**: Stellarium "modern" sky culture, CC BY-SA 4.0, drawn between the Hipparcos stars at their real 3D positions.
- **Galactic plane grid**: after the NASA/JPL-Caltech (R. Hurt) annotated Milky Way diagram; computed, not traced.
- **Sol**: planetary positions from the JPL approximate Keplerian elements (Standish, J2000 ± 2 centuries).
- **Star display names**: cross-checked during the build against taiyin-star-catalog-lite by RedSC1 (MPL-2.0); no code from it ships.

## Art

- **Planet textures**: Solar System Scope, https://www.solarsystemscope.com/textures/, CC BY 4.0 (Mercury, Venus, Earth day/night/specular, Moon, Mars, Jupiter, Saturn and rings, Uranus, Neptune).
- **Moon and dwarf-planet textures**: Io, Europa, Ganymede, Callisto, Enceladus and Pluto from NASA 3D Resources, https://github.com/nasa/NASA-3D-Resources (NASA/JPL-Caltech), free and without copyright under NASA's media usage guidelines. Resized to 1024x512 and no-data gaps filled with the local mean colour.
- **Holograms**: any body without a public texture, and every constructed system, is drawn as a hologram placeholder.
- **Galaxy, nebula and cluster rendering**: procedural, made for this project. The Halo rings are procedural models.
- **App icon**: made for this project.

## Software

- three.js r170, MIT, https://threejs.org/
- Tauri 2 and tauri-plugin-opener, MIT / Apache-2.0, https://tauri.app/
- Fonts: Inter (Rasmus Andersson), Chakra Petch (Cadson Demak), IBM Plex Mono (IBM), SIL Open Font Licence 1.1, bundled from fontsource 5.3.0; licence texts in app/fonts/.
