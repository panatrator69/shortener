"""Imports all pydantic.BaseModel subclasses. This avoids having to import from each submodule
within the dto package.
"""
# TODO there has to be a better way than just one import per class

from shortener.dto.create import Create, Response
