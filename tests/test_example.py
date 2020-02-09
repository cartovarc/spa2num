from spa2num.module import Template

def test_template():
  t = Template()
  assert t.say_hello() == "hello Christophe"
