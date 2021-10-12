import { Component, OnInit } from '@angular/core';
import { Category } from 'src/app/models/category.model';
import { CategoryService } from 'src/app/services/my-app.service';

@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrls: ['./category-list.component.css']
})
export class CategoryListComponent implements OnInit {

  category?: Category[];
  currentCategory: Category = {};
  currentIndex = -1;
  name = '';

  constructor(private categoryService: CategoryService) { }

  ngOnInit(): void {
    this.retrieveCategory();
  }

  retrieveCategory(): void {
    this.categoryService.getAll()
      .subscribe(
        data => {
          this.category = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveCategory();
    this.currentCategory = {};
    this.currentIndex = -1;
  }

  setActiveCategory(category: Category, index: number): void {
    this.currentCategory = category;
    this.currentIndex = index;
  }

  removeAllCategory(): void {
    this.categoryService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.refreshList();
        },
        error => {
          console.log(error);
        });
  }
}
