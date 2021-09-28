from app.back.src.main_back import Main_Back
from app.front.src.main_front import Main_Front

if __name__ == '__main__':
    print('========== TEST BACK ==========')
    main_back = Main_Back(test_ctrl=True)

    print('\n\n========== TEST FRONT ==========')
    main_front = Main_Front()
    print('...')
