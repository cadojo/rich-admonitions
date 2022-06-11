# `rich-admonitions`
_Markdown-like admonitions from the comfort of your terminal, all thanks to `rich`!_

> **Note**
>
> Credit where it's due! The structure of this project was set up with the 
> ever-helpful [PyScaffold](https://pyscaffold.org). And thanks to the 
> [Textualize](https://www.textualize.io) developers for their 
> [help](https://github.com/Textualize/rich/discussions/2051) with 
> debugging and developing this class!

## Overview

I think Julia's REPL admonitions are so neat.

```julia
julia> using Markdown

julia> md"""
       !!! note
           Check out this helpful note!
       """
  │ Note
  │
  │  Check out this helpful note!
```

Thanks to [`rich`](https://github.com/textualize/rich), it's not difficult to replicate this format with a Python class!

```python
>>> from admonitions import Admonition

>>> Admonition.note("Check out this helpful note!")
│ Note  
│
│  Check out this helpful note!   
```    

## Installation & Usage

This package is installable through the public PyPi index.

```bash
python -m pip install rich-admonitions
```

And it's use-able through the name `admonitions`!

```python
import admonitions
```

Any type that is renderable by `rich` can go in the `Admonition` constructor!

```python
>>> from rich.markdown import Markdown

>>> message = """
... # Mic Test
... 
... Testing, testing! Is this thing on?
... """

>>> Admonition(Markdown(message))

│ Notice  
│
│  ╔══════════════════════════════════════════════════════════════════════╗   
│  ║                               Mic Test                               ║   
│  ╚══════════════════════════════════════════════════════════════════════╝   
│                                                                             
│  Testing, testing! Is this thing on?                                        
```

And there a few out-of-the-box class methods to get you started. 😊

```python
>>> Admonition.note(
...     Admonition.tip(
...         Admonition.warning(
...             Admonition.danger(
...                 "Hold your breath! 🤿"
...             )
...         )
...     )
... )

│ Note  
│
│  │ Tip                                                                      
│  │                                                                          
│  │  │ Warning                                                               
│  │  │                                                                       
│  │  │  │ Danger                                                             
│  │  │  │                                                                    
│  │  │  │  Hold your breath! 🤿                                            
│  │  │                                                                       
│  │                                                                          
│    

```