<script setup>

</script>

<template>
	 <div class="box">
        <div class="forms">
            <div class="tips">
                <span class="login-btn">login</span>
                <span class="register-btn">register</span>
            </div>
            <div class="login">
                <div class="form-title">
                    <h1>Hello</h1>
                    <h4>One click triple connection</h4>
                </div>
                <div class="form">
                    <div class="username input-item">
                        <input type="text" class="ipts">
                    </div>
                    <div class="password input-item">
                        <input type="password" class="ipts">
                    </div>
                    <div class="other-select">
                        <div class="rem-pwd">
                            <input type="checkbox" id="check">
                            <label for="check" class="rem-pwd-tips">remember password</label>
                        </div>
                        <span class="fogot-pwd-btn">forgot password</span>
                    </div>
                    <button class="btn">Login</button>
                    <div class="other-login">
                        <span>Other login methods</span>
                        <div class="login-img">
                            <img src="/static/image/QQ.png" alt="">
                            <img src="/static/image/wechat-fill.png" alt="">
                        </div>
                    </div>
                </div>
            </div>
            <div class="register">
                <div class="form-title">
                    <h1>Register</h1>
                    <h4>One click triple connection</h4>
                </div>
                <div class="form">
                    <div class="username input-item">
                        <input type="text" class="ipts">
                    </div>
                    <div class="password input-item">
                        <input type="password" class="ipts">
                    </div>
                    <div class="conform-password input-item">
                        <input type="password" class="ipts">
                    </div>
                    <button class="btn">Register</button>
                </div>
            </div>
            <div class="fogot-pwd">
                <div class="form-title">
                    <h1>fogot-pwd</h1>
                    <h4>One click triple connection</h4>
                </div>
                <div class="form">
                    <div class="username input-item">
                        <input type="text" class="ipts">
                    </div>
                    <div class="password input-item">
                        <input type="password" class="ipts">
                    </div>
                    <div class="code input-item">
                        <input type="text" class="ipts">
                        <span class="veri-code-tips">Click To Get</span>
                    </div>
                    <button class="btn">Confirm</button>
                </div>
            </div>
        </div>

    </div>
</template>

<style scoped>
@import "../assets/login.css";
h1 {
    font-size: 2em;
}
</style>