import pynecone as pc

class MakibotdocsConfig(pc.Config):
    pass

config = MakibotdocsConfig(
    app_name="MakiBot_docs",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
