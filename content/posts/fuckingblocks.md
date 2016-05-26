Title: iOS block定义
Date: 2016-05-20
Tags: iOS
Category: iOS
Slug: fuckingblocks

##How Do I Declare A Block in Objective-C?

```objc
As a local variable:

returnType (^blockName)(parameterTypes) = ^returnType(parameters) {...};
As a property:

@property (nonatomic, copy, nullability) returnType (^blockName)(parameterTypes);
As a method parameter:

- (void)someMethodThatTakesABlock:(returnType (^nullability)(parameterTypes))blockName;
As an argument to a method call:

[someObject someMethodThatTakesABlock:^returnType (parameters) {...}];
As a typedef:

typedef returnType (^TypeName)(parameterTypes);
TypeName blockName = ^returnType(parameters) {...};
```

取自：<http://fuckingblocksyntax.com/>
