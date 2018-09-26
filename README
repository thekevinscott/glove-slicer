# GLoVE Slicer

Downloads the [GLoVE word embeddings](https://nlp.stanford.edu/projects/glove/) and slices them into smaller chunks.

```
python slice.py --embeddings glove.6B --chunk_size 500 --target
chunked_embeddings
```

This will produce an output folder of `chunked_embeddings`, containing:

* a list of txt files with 500 lines each
* a `manifest.json` detailing the chunk size and array of files with names and start indices
* a `word_manifest.json` listing which words are in which file
