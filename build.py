from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="SpaceIm", channel="testing", build_policy="missing", skip_check_credentials=True)
    builder.add_common_builds(pure_c=True, dll_with_static_runtime=True, build_all_options_values=None)
    builder.run()
