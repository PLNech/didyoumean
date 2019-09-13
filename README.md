# didYouMean

didYouMean is Python module that you can use to correct spelling mistakes. It leverages Google Translate's "Did You Mean" feature, detecting the input language unless you specify one.

## Requirements
- Python3
- `selenium`

## Usage
```bash
python didYouMean.py "fotball"
> football
python didYouMean.py "football"
> football
python didYouMean.py "ich bin mude" "de"
> ich bin müde
```

```python
from didyoumean3.didyoumean import did_you_mean
did_you_mean("fotball") # -> football
did_you_mean("football") # -> football
did_you_mean("ich bin mude") # -> ich bin müde
```

# Credits
Adapted by [@PLNech](https://github.com/PLNech) based on the work by [@bkvirendra](https://github.com/bkvirendra).

# License

DidYouMean3 is [free software under the Gnu GPLv3 license](./LICENSE).
