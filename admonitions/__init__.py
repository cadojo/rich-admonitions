"""Markdown-like admonitions in the comfort of your terminal!

Thanks to the excellant `rich`, Julia-style `Markdown` admonitions
are super easy to set up in Python.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("rich-admonitions")
except PackageNotFoundError:
    __version__ = "unknown"


# Items to "export" from this module!
__export__ = {
    "Admonition",
}

from dataclasses import dataclass
from typing import Iterable, Union
from rich.segment import Segment
from rich.style import Style
from rich.text import Text
from rich.padding import Padding
from rich.console import Console, ConsoleOptions, Measurement, RenderableType


@dataclass
class Admonition:
    """
    A rich-text formatted admonition, with built-in themes!
    """

    content: Union[str, RenderableType]
    header: Union[str, Text] = "Notice"
    style: Union[str, Style] = "bold"
    markup: bool = True

    def __init__(
        self,
        content: Union[str, RenderableType] = "...",
        header: Union[str, Text] = "Notice",
        style: Union[str, Style] = "bold blue",
        markup: bool = True,
    ):
        self.content = content
        self.header = header
        self.style = style
        self.markup = markup

    def __str__(self) -> str:
        """Render the message as a str."""
        return str(self.content)

    def __repr__(self) -> str:
        return f"Banner(content={self.content}, header={self.header}, style={self.style}, markup={self.markup})"

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> Iterable[Segment]:
        """Render the message as a rich string."""
        from rich.segment import Segment
        from rich.text import Text

        yield from self.render(
            content=Text(self.header, style=self.style, end="")
            if isinstance(self.header, str)
            else self.header,
            console=console,
            markup=self.markup,
            style=self.style,
            space=1,
        )
        yield self.prefix(style=console.get_style(self.style))
        yield Segment.line()
        yield from self.render(
            content=self.content,
            console=console,
            markup=self.markup,
            style=self.style,
            space=2,
        )
        yield Segment.line()

    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement:
        """Measure the message."""
        from math import floor
        from rich.measure import Measurement

        return Measurement(
            floor(len(self.header) * 1.25) if self.header else 8, options.max_width
        )

    @classmethod
    def note(
        cls,
        content: RenderableType,
        header: str = "Note",
        style: Union[str, Style] = "bold magenta3",
        **kwargs,
    ) -> "Admonition":
        """A note message."""
        return cls(content, header, style, **kwargs)

    @classmethod
    def tip(
        cls,
        content: RenderableType,
        header: str = "Tip",
        style: Union[str, Style] = "bold green",
        **kwargs,
    ) -> "Admonition":
        """A tip message."""
        return cls(content, header, style, **kwargs)

    @classmethod
    def info(
        cls,
        content: RenderableType,
        header: str = "Info",
        style: Union[str, Style] = "bold cyan",
        **kwargs,
    ) -> "Admonition":
        """An info message."""
        return cls(content, header, style, **kwargs)

    @classmethod
    def warning(
        cls,
        content: RenderableType,
        header: str = "Warning",
        style: Union[str, Style] = "bold orange3",
        **kwargs,
    ) -> "Admonition":
        """A warning message."""
        return cls(content, header, style, **kwargs)

    @classmethod
    def danger(
        cls,
        content: RenderableType,
        header: str = "Danger",
        style: Union[str, Style] = "bold red",
        **kwargs,
    ) -> "Admonition":
        """A danger message."""
        return cls(content, header, style, **kwargs)

    @classmethod
    def prefix(cls, style: Style = Style(bold=True)) -> Segment:
        """Return the default message prefix character."""
        from rich.segment import Segment

        return Segment("│", style=style)

    @classmethod
    def render(
        cls,
        content: RenderableType,
        console: Console,
        markup: bool = False,
        options: Union[ConsoleOptions, None] = None,
        style: Union[str, Style] = "bold",
        space: int = 2,
    ) -> Iterable[Segment]:
        """Render the message as a rich string."""
        from rich.text import Text
        from rich.padding import Padding

        _style = console.get_style(style)
        _options = options if options else console.options

        if isinstance(content, str):
            if markup:
                _content: Union[Text, RenderableType] = Text.from_markup(content, end="")
            else:
                _content = Text(content, end="")
        else:
            _content = content

        for line in console.render_lines(
            Padding(_content, (0, space + 1, 0, space), expand=False),
            options=_options.update_width(console.width - space - 1),
            new_lines=True,
            pad=False,
        ):
            yield cls.prefix(style=_style)
            yield from line


if __name__ != "__main__":
    for _ in (*locals(), "_"):
        if not _.startswith("__") and _ not in __export__:
            del locals()[_]