import unittest

from anthrax.container import Form
from anthrax.html_input.field import HtmlField
from util import dummy_frontend

class Test(unittest.TestCase):
    """Test basic form features"""

    def setUp(self):
        class TestForm(Form):
            __frontend__ = dummy_frontend
            text = HtmlField(
                tag_whitelist = [
                    'p',
                    ('span', ['class', 'id']),
                    ('b', []),
                ]
            )
        self.form = TestForm()

    def test_valid(self):
        """Testing a valid input"""
        self.form.__raw__ = {
            'text': """<p class="knight">
<span class="name">Sir <b>Galahad</b></span> The Pure
</p>"""
        }
        self.assertTrue(self.form.__valid__)
        self.assertEqual(self.form['text'].tag, 'p')
