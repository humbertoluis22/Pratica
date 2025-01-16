from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column,registry

reg = registry()

@reg.mapped_as_dataclass
class Comment:
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(init=False,primary_key=True)
    name:Mapped[str]
    comment : Mapped[str]
    live : Mapped[str]
    created_at : Mapped[datetime] = mapped_column(
        init=False,server_default=func.now()
    )

# formas de criar uma tabela