__version__ = "2.7.0"

def get_version(version_length=2, placeholder="x"):
    release = __version__

    version = ".".join(release.split(".", version_length)[:version_length])

    if placeholder:
        version = "{}.{}".format(version, placeholder)

    return version, release

version, release = get_version(placeholder=23)

print(version)
print(release)
