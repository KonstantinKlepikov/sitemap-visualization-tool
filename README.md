# Visualizing an XML sitemap using Python

Source code repository for the ["How to visualize an XML sitemap using Python"](https://www.ayima.com/guides/how-to-visualize-an-xml-sitemap-using-python.html) Ayima blog post.

![sitemap_graph_2_layer](research/static/sitemap_graph_2_layer.png)

## Extraction, Categorization and Visualization

The code has been split into three scripts that can be [downloaded here](https://github.com/Ayima/sitemap-visualization-tool/archive/master.zip). Running these requires Python and external library dependencies as detailed in the section below.

### Reproducing our Results

Before plugging in a new sitemap, you may wish to test the script by reproducing a result from our blog post. This can be done by opening a terminal session, navigating to the folder containing the three `.py` scripts and running the following commands:

```shell
python extract_urls.py   
python categorize_urls.py   
python visualize_urls.py --depth 1   
```

### Plugging in an XML Sitemap URL

A custom sitemap URL can be ingested by passing arguments to the extraction script. The commands to execute would look something like this (where we are categorizing and visualizing with a granularity depth of 3):

```shell
python extract_urls.py --url "site.com/sitemap-index.xml"
python categorize_urls.py --depth 3   
python visualize_urls.py --depth 3 --title "My Sitemap" --size "20"
```

If your XML sitemap file contains the page URLs (instead of linking to other sitemaps) then make sure to pass the `--not_index` argument:

```shell
python extract_urls.py --url "site.com/sitemap.xml" --not_index
```

There is also built in support for compressed XML files:

```shell
python extract_urls.py --url "site.com/sitemap.xml" --not_index --gzip
```

The `visualize_urls.py` script also has a `--limit` argument that can be passed. This can be used to limit the number of edges spawning from a node, and is useful for creating deep sitemap visualizations that don't grow out of control. For example:

```shell
python categorize_urls.py --depth 6
python visualize_urls.py --depth 6 --limit 2 --size "30"
```

The graph save format can be specified with `--output-format` e.g. `python visualize_urls.py --output-format png`.

Additionally, select nodes can be skipped (restrict children from rendering) using the `--skip` argument. For example:

```shell
python extract_urls.py
python categorize_urls.py
python visualize_urls.py --depth 2 --skip 'product,brands,categories,find,campaigns,clearance,stores'   
```

More detailed usage instructions are included in the header of each file.

### Categorizing and Visualizing a list of URLs

If you already have a list of URLs, they can be compiled into a file named `sitemap_urls.dat` that contains one URL per line, and then processed by running the latter two scripts:

```shell
python categorize_urls.py
python visualize_urls.py
```

Please ensure you have installed the dependencies before attempting to run the scripts.

## Dependencies

The code can run in Python 2 or 3 and the external library dependencies are as follows:

- Requests and BeautifulSoup4 for `extract_urls.py`
- Pandas for `categorize_urls.py`
- Graphviz for `visualize_urls.py`

Open folder of this project and install python dependencies:

`virtualenv -p python 3.8 venv`

`source venv/bin/activate`

`pip install  -r requirements.txt`

Development mode:

`pip install -e .`

For `jupyter_contrib_nbextensions` folow [activation guide](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)

___

### Contact

We are here to help! If you run into any problems you can reach out to us on twitter [@ayima](http://twitter.com/ayima).
