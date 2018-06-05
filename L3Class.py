
public_var = 12
_private_var = 34

__all__ = ['public_var','_private_var','_private_fun']

def public_fun():
    sum_pub_priv = public_var + _private_var
    print('This function is public. The sum is ', sum_pub_priv)
    
def _private_fun():
    print('... now this function is set to be private')
    
class PublicClass():
    print('This is public class')
class _PrivateClass():
    print('... now this Class is private')

