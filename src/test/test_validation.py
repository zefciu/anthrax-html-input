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

    def test_illegal_tag(self):
        """Testing an input with illegal tag"""
        self.form.__raw__ = {
            'text': """<p class="knight">
<span class="name">Sir <b>Galahad</b></span> <i>The Pure</i>
</p>"""
        }
        self.assertFalse(self.form.__valid__)
        self.assertEqual(
            self.form.__errors__['text'].message,
            'Tag i is not allowed',
        )

    def test_illegal_attrib1(self):
        """Testing an input with illegal attribute (other available)"""
        self.form.__raw__ = {
            'text': """<p class="knight">
<span style="color: red;">Sir <b>Galahad</b></span> The Pure
</p>"""
        }
        self.assertFalse(self.form.__valid__)
        self.assertEqual(
            self.form.__errors__['text'].message,
            'Attribute style not allowed in tag span',
        )

    def test_illegal_attrib2(self):
        """Testing an input with illegal attribute (empty attrib whitelist)"""
        self.form.__raw__ = {
            'text': """<p class="knight">
<span class="name">Sir <b id="x">Galahad</b></span> The Pure
</p>"""
        }
        self.assertFalse(self.form.__valid__)
        self.assertEqual(
            self.form.__errors__['text'].message,
            'Attribute id not allowed in tag b',
        )
