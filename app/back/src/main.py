from app.back.src.init import Init


def main(test_pico_connection=False):
    return Init()(test_pico_connection)
