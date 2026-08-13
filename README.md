# Posters

Here we collect project, conference and workshop posters. 
You can find empty templates for the workshop posters as svg (editable with e.g. InkScape) and pdf (you could add your info with e.g. Powerpoint or Photoshop etc.).

Required fonts for some posters:
- Allegre Sans
- Futura LtCn BT
- sans-serif


Converting RGB pdf to CMYK pdf:
```
$ gs \
  -o poster-cmyk.pdf \
  -sDEVICE=pdfwrite \
  -sProcessColorModel=DeviceCMYK \
  -sColorConversionStrategy=CMYK \
  -sColorConversionStrategyForImages=CMYK \
   poster-rgb.pdf 
```

## Wordcloud

A small python script is provided to generate a wordcloud.
ATM it can generate only PNG images. 
