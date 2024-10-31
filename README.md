# Notebooks to process organoid movies
AC project

### create_organoid_projections_from_tiles_scrambled_file.ipynb

- input: lif file containing z-stacks
- output: tif files for each channel and frame (in temp dir)

### stitch_and_align.ipynb

- input: tif files for each channel and frame (from temp dir)
- output: aligned movies (in 'movies' dir)

- if successful - remove the temp dir
- if unsuccessful - use:

### when_ashlar_fails.ipynb (optional)

- input: tif files for each channel and frame (from temp dir)
- output: aligned movies (in 'movies' dir)

### save_separate_organoids.ipynb

- input: tif movies for each channel
- output: tif movies of each organoid separately


## Other tools:

### create_organoid_projections.ipynb

- input: lif file containing z-stacks
- output: tif files with projections (movies) for each channel
