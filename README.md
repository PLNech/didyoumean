# didYouMean

didYouMean is Python module that you can use to correct spelling mistakes. It leverages Google's "Did You Mean" feature.

## Requirements
- Python3
- `beautifulsoup4==4.8.0`

## Usage
```bash
python didYouMean.py "fotball"
> football
python didYouMean.py "football"
> football
```

```python
from didYouMean3 import didYouMean
didYouMean("fotball") # -> football
didYouMean("fotball") # -> football
```

# Credits
Adapted by [@PLNech](https://github.com/PLNech) based on the work by [@bkvirendra](https://github.com/bkvirendra).

# License

DidYouMean3 is [free software under the Gnu GPLv3 license](./LICENSE).