from traitlets.config import LoggingConfigurable
from traitlets.traitlets import Unicode


class NotebookGist(LoggingConfigurable):

    oauth_client_id = Unicode(
        '',
        config=True,
        help='The GitHub application OAUTH client ID',
    )

    oauth_client_secret = Unicode(
        '',
        config=True,
        help='The GitHub application OAUTH client secret',
    )

    def __init__(self, *args, **kwargs):
        self.config_manager = kwargs.pop('config_manager')
        super(NotebookGist, self).__init__(*args, **kwargs)
        # update the frontend settings with the currently passed
        # OAUTH client id
        self.config_manager.update('notebook', {
            'oauth_client_id': self.config.NotebookGist.oauth_client_id,
        })
