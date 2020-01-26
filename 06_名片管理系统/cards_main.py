#! /usr/bin/python3

import cards_tools

while True:  # 无限循环，由用户主动决定什么时候退出循环！

    # 在#后跟上TODO，用于标记需要去做的工作
    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您做出的选择是【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:  # 使用in针对列表判断，避免使用or拼接复杂的逻辑条件
        # 如果在开发程序时，不希望立刻编写分支内部的代码
        # 可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确！
        # 程序运行时，pass 关键字不会执行任何的操作！

        # 1 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 2 显示所有名片
        elif action_str == "2":
            cards_tools.show_all()
        # 3 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】，再见！")
        break

    # 其他 错误输入，需要提示用户
    else:
        print("您输入的不正确，请重新选择")
