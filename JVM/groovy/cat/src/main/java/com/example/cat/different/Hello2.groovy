package com.example.cat.different

import static junit.framework.TestCase.assertEquals


int method(String arg) {

    return 1

}

int method(Object arg) {
    return 2
}


Object o = "Object"

int result = method(o)
assertEquals(2, result)


