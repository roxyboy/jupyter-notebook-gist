### jupyter-notebook-gist

Create a gist from the Jupyter Notebook UI.

## Installation

To install, simply run:

```
pip install jupyter-notebook-gist
jupyter serverextension enable --py jupyter_notebook_gist
jupyter nbextension install --py jupyter_notebook_gist
jupyter nbextension enable --py jupyter_notebook_gist
```
To double-check if the extension was correctly installed run:

```
jupyter nbextension list
jupyter serverextension list
```

To uninstall the extension run:

```
jupyter serverextension disable --py jupyter_notebook_gist
jupyter nbextension disable --py jupyter_notebook_gist
jupyter nbextension uninstall --py jupyter_notebook_gist
pip uninstall jupyter-notebook-gist
```

## Configuration

After installing, edit your `jupyter_notebook_config.py` file to specify the
GitHub client id and secret.

If your `jupyter_notebook_config.py` file does not exist, you can create one by
running `jupyter notebook --generate-config`. You can check the location of
this file by running `jupyter --config-dir`.

```python
c.NotebookGist.oauth_client_id = "my_client_id"         # FIXME
c.NotebookGist.oauth_client_secret = "my_client_secret" # FIXME
```

Replace the vars above with a working GitHub client id and secret. You can
create one [here](https://github.com/settings/applications).

Here's an [example of an OAuth application](https://cloud.githubusercontent.com/assets/969479/14916551/add90efc-0df0-11e6-8cfb-277754a48b66.png)
created by @mreid-moz for testing.

Then run `jupyter notebook` from the repo root.

Alternatively you can also pass the GitHub client id and secret as command
line parameters when you run the notebook (please fill the placeholders
accordingly):

```
jupyter notebook --NotebookGist.oauth_client_id="<my_client_id>" --NotebookGist.oauth_client_secret="<my_client_secret>"
```
